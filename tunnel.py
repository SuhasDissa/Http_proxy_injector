import socket 
import time
import select
import threading
#from inject import injector
import configparser
import ssl
from subprocess import Popen

bg=''
G = bg+'\033[32m'
O = bg+'\033[33m'
GR = bg+'\033[37m'
R = bg+'\033[31m'

class injector:
	def __init__(self):
		pass

	def conf(self):
		config = configparser.ConfigParser()
		try:
			config.read_file(open('settings.ini'))
		except Exception as e:
			self.logs(e)
		return config

	def getpayload(self,config):
		payload = config['config']['payload']
		return payload 

	def proxy(self,config):
	    proxyhost = config['config']['proxyip']
	    proxyport = int(config['config']['proxyport'])
	    return [proxyhost,proxyport]
	def conn_mode(self,config):
		mode = config['mode']['connection_mode']
		return mode

	def auto_rep(self,config):
		result = config['config']['auto_replace']
		return result


	def payloadformating(self,payload,host,port):
		payload = payload.replace('[crlf]','\r\n')
		payload = payload.replace('[crlf*2]','\r\n\r\n')
		payload = payload.replace('[cr]','\r')
		payload = payload.replace('[lf]','\n')
		payload = payload.replace('[protocol]','HTTP/1.0')
		payload = payload.replace('[ua]','Dalvik/2.1.0')  
		payload = payload.replace('[raw]','CONNECT '+host+':'+port+' HTTP/1.0\r\n\r\n')
		payload = payload.replace('[real_raw]','CONNECT '+host+':'+port+' HTTP/1.0\r\n\r\n') 
		payload = payload.replace('[netData]','CONNECT '+host+':'+port +' HTTP/1.0')
		payload = payload.replace('[realData]','CONNECT '+host+':'+port+' HTTP/1.0')	
		payload = payload.replace('[split_delay]','[delay_split]')
		payload = payload.replace('[split_instant]','[instant_split]')
		payload = payload.replace('[method]','CONNECT')
		payload = payload.replace('mip','127.0.0.1')
		payload = payload.replace('[ssh]',host+':'+port)
		payload = payload.replace('[lfcr]','\n\r')
		payload = payload.replace('[host_port]',host+':'+port)
		payload = payload.replace('[host]',host)
		payload = payload.replace('[port]',port)
		payload = payload.replace('[auth]','')
		return payload

	def connection(self,client, s,host,port):
	        if int(self.conn_mode(self.conf())) == 0:
	        	payload = f'CONNECT {host}:{port} HTTP/1.0\r\n\r\n'
	        else:
	        	payload = self.payloadformating(self.getpayload(self.conf()),host,port)
	        
	        if '[split]' in payload or '[instant_split]' in payload or '[delay_split]' in payload:
	          payload = payload.replace('[split]'        ,'||1.0||')
	          payload = payload.replace('[delay_split]'  ,'||1.5||')
	          payload = payload.replace('[instant_split]','||0.0||')
	          req = payload.split('||')
	          for payl in req:
	              if ('0.5' == payl or  '1.5' == payl or '0.0' == payl) :
	                delay = payl
	                time.sleep(float(delay))
	              else:
	                s.send(payl.encode())
	        
	        elif '[repeat_split]' in payload  :
	          payload = payload.replace('[repeat_split]','||1||')
	          payload = payload.replace('[x-split]','||1||')
	          req = payload.split('||')
	          payl = []
	          for element in req:
	            if element and element == '1' :pass
	            else:payl.append(element)
	          rpspli = payl[0]+payl[0]
	          s.send(rpspli.encode())
	          s.send(payl[1].encode())

	        elif '[reverse_split]' in payload or '[x-split]' in payload:
	          payload = payload.replace('[reverse_split]','||2|')
	          payload = payload.replace('[x-split]','||2|')
	          req = payload.split('||')
	          payl = []
	          for element in req:
	            if element and element == '2':pass
	            else:payl.append(element)
	          rvsplit = payl[0]+payl[1]
	          s.send(rvsplit.encode())
	          s.send(payl[1].encode())

	        elif '[split-x]' in payload:
	          payload = payload.replace('[split-x]','||3||')
	          req = payload.split('||')
	          xsplit = []
	          for element in req:
	            if element and element == '3':pass
	            else:xsplit.append(element)
	          alpay = xsplit[0]+xsplit[1]
	          s.send(alpay.encode())
	          
	          time.sleep(1.0)
	          s.send(xsplit[1].encode())
	        else:
	          
	          s.send(payload.encode())
	        
	        if int(self.auto_rep(self.conf())) == 1 or int(self.auto_rep(self.conf())) == 2:
	        	status = s.recv(1024).split('\n'.encode())[0]
	        	self.logs(status.decode())
	       
	        client.send(b"HTTP/1.1 200 Connection Established\r\n\r\n")
	        if int(self.auto_rep(self.conf())) == 2:
	        	status = s.recv(1024).split('\n'.encode())[0]
	        	self.logs(status.decode())
	       
	        
	        
	def logs(self,log):
		print(log)
class Tun(injector):
	def __init__(self):
		self.localip = '127.0.0.1'
		self.LISTEN_PORT = 9092

	def conf(self):
		config = configparser.ConfigParser()
		try:
			config.read_file(open('settings.ini'))
		except Exception as e:
			self.logs(e)
		return config
	def extraxt_sni(self,config):
		sni = config['sni']['server_name']
		return sni
	def proxy(self,config):
	    proxyhost = config['config']['proxyip']
	    proxyport = int(config['config']['proxyport'])
	    return [proxyhost,proxyport]
	def conn_mode(self,config):
		mode = config['mode']['connection_mode']
		return mode
	def tunneling(self,client,sockt):
		connected = True
		while connected == True:
			r, w, x = select.select([client,sockt], [], [client,sockt],3)
			if x: connected = False; break
			for i in r:
				try:
					data = i.recv(8192)
					if not data: connected = False; break
					if i is sockt:
						client.send(data)
					else:
						sockt.send(data)
				except:
					connected = False;break
		client.close()
		sockt.close()
		self.logs(R+'Disconnected '+GR)
	def destination(self,client, address):
	    try:
	        self.logs(G+'<#> Client {} received!{}'.format(address[-1],GR)) 
	        request = client.recv(9124).decode()
	        host = request.split(':')[0].split()[-1]
	        port = request.split(':')[-1].split()[0]
	        try:
	            proxip=self.proxy(self.conf())[0] 
	            proxport=self.proxy(self.conf())[1]
	        except ValueError:
	        	proxip = host
	        	proxport = port
	        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	        s.connect((proxip,int(proxport)))
	        self.logs(f'{G}connected to {proxip}:{proxport}{GR}')
	        if int(self.conn_mode(self.conf())) == 2:
	        	SNI_HOST = self.extraxt_sni(self.conf())
	        	context = ssl.SSLContext(ssl.PROTOCOL_TLS)
	        	s = context.wrap_socket(s,server_hostname=str(SNI_HOST))
	        	self.logs(f'Handshaked successfully to {SNI_HOST}')
	        	self.logs(f"protocol : {context.get_ciphers()[0]['protocol']}")
	        	client.send(b"HTTP/1.1 200 Connection Established\r\n\r\n")
	        elif int(self.conn_mode(self.conf())) == 3:
	        	SNI_HOST = self.extraxt_sni(self.conf())
	        	context = ssl.SSLContext(ssl.PROTOCOL_TLS)
	        	s = context.wrap_socket(s,server_hostname=str(SNI_HOST))
	        	self.logs(f'Handshaked successfully to {SNI_HOST}')
	        	self.logs(f"protocol : {context.get_ciphers()[0]['protocol']}")
	        	injector.connection(self,client, s,str(host),str(port))
	        else:
	        	injector.connection(self,client, s,str(host),str(port))


	        self.tunneling(client,s)
	    except Exception as e:
	    	self.logs(f'{G}{e}{GR}')
	def create_connection(self):
		try:
		    sockt = socket.socket()
		    sockt.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		    sockt.bind(('', self.LISTEN_PORT))
		    sockt.listen(0)
		    
		    self.logs('Waiting for incoming connection to : {}:{}\n'.format(self.localip,self.LISTEN_PORT))
		except OSError:
		    self.logs(O+'Port already used by another process\nRun script again'+GR)
		    
		    
		    
		while True:
		    try:
		        client, address = sockt.accept()
		        thr = threading.Thread(target=self.destination, args=(client, address))
		        thr.start()
		        
		    except KeyboardInterrupt:
		        sockt.close()
		        
		        
		sockt.close()
	def logs(self,log):
		print(log)
if __name__=='__main__':
	start = Tun()
	start.create_connection()
