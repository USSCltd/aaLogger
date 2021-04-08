import sys,os
sys.path.append( os.path.dirname( os.path.abspath(__file__) ) + r'\..\sulley' )
from sulley import *
from requests import aalogger

uuid0 = "4e0c90df-e39d-4164-a421-ace89484c602"
ver0 = "1.0"
uuid = ""
ver = ""

def rpc_bind( sock, uuid, ver, is_alter_context=False ):
	utils.dcerpc.call_id += 1
	print "RPC BIND {UUID} {VER}".format( UUID=uuid, VER=ver )
	if is_alter_context:
		data_bind = utils.dcerpc.bind( uuid, ver, 1, is_alter_context=is_alter_context )
	else:
		data_bind = utils.dcerpc.bind( uuid, ver, 2 )
	sock.send( data_bind )
	utils.dcerpc.bind_ack( sock.recv( 1024 ) )

def rpc_request_context_handle( sock, opnum ):
	print "RPC REQUEST op: {opnum} ObjUUID: {object_uuid}".format( opnum=opnum, object_uuid=aalogger.object_uuid )
	data_request = utils.dcerpc.request( aalogger.object_uuid, opnum, '' )
	#print 'send request: {hex}'.format( hex=data_request.encode('hex') )
	sock.send( data_request )
	data_ans = sock.recv( 1024 )
	#print 'recv: {hex}'.format( hex=data_ans.encode('hex') )
	return utils.dcerpc.get_context_handle(data_ans)

def rpc_init( sock ):
	utils.dcerpc.context_id = 0
	rpc_bind(sock, uuid0, ver0)
	context_handle = rpc_request_context_handle(sock, 0)
	s_get("iface1_proc0").names["context_handle"].value = context_handle
	s_get("iface1_proc1").names["context_handle"].value = context_handle
	s_get("iface1_proc2").names["context_handle"].value = context_handle
	s_get("iface1_proc3").names["context_handle"].value = context_handle
	s_get("iface1_proc4").names["context_handle"].value = context_handle
	s_get("iface1_proc5").names["context_handle"].value = context_handle

	s_get("iface2_proc0").names["context_handle"].value = context_handle
	s_get("iface2_proc1").names["context_handle"].value = context_handle
	s_get("iface2_proc2").names["context_handle"].value = context_handle

	s_get("iface3_proc0").names["context_handle"].value = context_handle
	s_get("iface3_proc1").names["context_handle"].value = context_handle
	s_get("iface3_proc2").names["context_handle"].value = context_handle
	s_get("iface3_proc3").names["context_handle"].value = context_handle
	s_get("iface3_proc5").names["context_handle"].value = context_handle
	s_get("iface3_proc6").names["context_handle"].value = context_handle
	s_get("iface3_proc7").names["context_handle"].value = context_handle
	s_get("iface3_proc10").names["context_handle"].value = context_handle
	s_get("iface3_proc11").names["context_handle"].value = context_handle
	s_get("iface3_proc12").names["context_handle"].value = context_handle
	s_get("iface3_proc13").names["context_handle"].value = context_handle
	s_get("iface3_proc14").names["context_handle"].value = context_handle

	s_get("iface4_proc0").names["context_handle"].value = context_handle
	s_get("iface4_proc1").names["context_handle"].value = context_handle
	s_get("iface4_proc2").names["context_handle"].value = context_handle
	s_get("iface4_proc3").names["context_handle"].value = context_handle
	s_get("iface4_proc5").names["context_handle"].value = context_handle
	s_get("iface4_proc6").names["context_handle"].value = context_handle
	s_get("iface4_proc7").names["context_handle"].value = context_handle
	s_get("iface4_proc10").names["context_handle"].value = context_handle
	s_get("iface4_proc11").names["context_handle"].value = context_handle
	s_get("iface4_proc12").names["context_handle"].value = context_handle
	s_get("iface4_proc13").names["context_handle"].value = context_handle
	s_get("iface4_proc14").names["context_handle"].value = context_handle

	s_get("iface5_proc0").names["context_handle"].value = context_handle
	s_get("iface5_proc1").names["context_handle"].value = context_handle
	s_get("iface5_proc2").names["context_handle"].value = context_handle
	s_get("iface5_proc3").names["context_handle"].value = context_handle
	s_get("iface5_proc5").names["context_handle"].value = context_handle
	s_get("iface5_proc6").names["context_handle"].value = context_handle
	s_get("iface5_proc7").names["context_handle"].value = context_handle
	s_get("iface5_proc10").names["context_handle"].value = context_handle
	s_get("iface5_proc11").names["context_handle"].value = context_handle
	s_get("iface5_proc12").names["context_handle"].value = context_handle
	s_get("iface5_proc13").names["context_handle"].value = context_handle
	s_get("iface5_proc14").names["context_handle"].value = context_handle

	s_get("iface6_proc2").names["context_handle"].value = context_handle
	s_get("iface6_proc3").names["context_handle"].value = context_handle
	s_get("iface6_proc4").names["context_handle"].value = context_handle
	s_get("iface6_proc5").names["context_handle"].value = context_handle

	s_get("iface7_proc2").names["context_handle"].value = context_handle
	s_get("iface7_proc3").names["context_handle"].value = context_handle
	s_get("iface7_proc4").names["context_handle"].value = context_handle
	s_get("iface7_proc5").names["context_handle"].value = context_handle
	s_get("iface7_proc7").names["context_handle"].value = context_handle
	s_get("iface7_proc8").names["context_handle"].value = context_handle

	s_get("iface8_proc2").names["context_handle"].value = context_handle
	s_get("iface8_proc3").names["context_handle"].value = context_handle
	s_get("iface8_proc8").names["context_handle"].value = context_handle
	print "context_handle=%s" % context_handle.encode('hex')
	utils.dcerpc.context_id += 2
	#utils.dcerpc.call_id += 1
	rpc_bind(sock, uuid, ver, is_alter_context=True)


def iface1(ip, port, **opts):
	global uuid,ver
	uuid = opts['uuid']
	ver = opts['ver']
	aalogger.object_uuid = opts['object_uuid']
	sess = sessions.session( session_filename="audits/aaLogger_iface1_fuzz.session", sleep_time=1, timeout=1 )
	#sess = sessions.session(  )
	target = sessions.target( ip, port )
	
	#target.netmon = sulley.pedrpc.client("127.0.0.1", 26001)
	target.procmon = sulley.pedrpc.client("127.0.0.1", 28001)
	target.procmon_options = {
		"proc_name": "aalogger_patched.exe",
		"stop_commands": ["TERMINATE_PID"],
		"start_commands": ["net start aalogger_patched"]
	}
	aalogger.procmon = target.procmon
	aalogger.session = sess
	target.procmon.set_ifname("iface1")
	
	sess.add_target( target )
	sess.pre_send = rpc_init

	sess.connect( s_get("iface1_proc0") )
	sess.connect( s_get("iface1_proc1") )
	sess.connect( s_get("iface1_proc2") )
	sess.connect( s_get("iface1_proc3") )
	sess.connect( s_get("iface1_proc4") )
	sess.connect( s_get("iface1_proc5") )
	
	with open("audits/iface1_graph.udg", "w+") as o:
		o.write( sess.render_graph_udraw() )

	sess.fuzz()

def iface2(ip, port, **opts):
	global uuid,ver
	uuid = opts['uuid']
	ver = opts['ver']
	aalogger.object_uuid = opts['object_uuid']
	sess = sessions.session( session_filename="audits/aaLogger_iface2_fuzz.session", sleep_time=1, timeout=1 )
	#sess = sessions.session(  )
	target = sessions.target( ip, port )
	
	#target.netmon = sulley.pedrpc.client("127.0.0.1", 26002)
	target.procmon = sulley.pedrpc.client("127.0.0.1", 28001)
	target.procmon_options = {
		"proc_name": "aalogger_patched.exe",
		"stop_commands": ["TERMINATE_PID"],
		"start_commands": ["net start aalogger_patched"]
	}
	aalogger.procmon = target.procmon
	aalogger.session = sess
	target.procmon.set_ifname("iface2")
	
	sess.add_target( target )
	sess.pre_send = rpc_init

	#sess.connect( s_get("iface2_proc0") )
	sess.connect( s_get("iface2_proc1") )
	#sess.connect( s_get("iface2_proc2") )
	
	with open("audits/iface2_graph.udg", "w+") as o:
		o.write( sess.render_graph_udraw() )

	sess.fuzz()

def iface3(ip, port, **opts):
	global uuid,ver
	uuid = opts['uuid']
	ver = opts['ver']
	aalogger.object_uuid = opts['object_uuid']
	sess = sessions.session( session_filename="audits/aaLogger_iface3_fuzz.session", sleep_time=1, timeout=1 )
	#sess = sessions.session(  )
	target = sessions.target( ip, port )
	
	#target.netmon = sulley.pedrpc.client("127.0.0.1", 26003)
	target.procmon = sulley.pedrpc.client("127.0.0.1", 28001)
	target.procmon_options = {
		"proc_name": "aalogger_patched.exe",
		"stop_commands": ["TERMINATE_PID"],
		"start_commands": ["net start aalogger_patched"]
	}
	aalogger.procmon = target.procmon
	aalogger.session = sess
	target.procmon.set_ifname("iface3")
	
	sess.add_target( target )
	sess.pre_send = rpc_init

	sess.connect( s_get("iface3_proc0") )
	#sess.connect( s_get("iface3_proc0"), s_get("iface3_proc1") )	# 140
	#sess.connect( s_get("iface3_proc0"), s_get("iface3_proc2") )	# 140
	#sess.connect( s_get("iface3_proc0"), s_get("iface3_proc3") )	# 560
	#sess.connect( s_get("iface3_proc0"), s_get("iface3_proc4") )	# 0
	#sess.connect( s_get("iface3_proc0"), s_get("iface3_proc5") )	# 5928	AV: 3402, 3403, 5613, 5614
	#sess.connect( s_get("iface3_proc0"), s_get("iface3_proc6") )	# 140
	#sess.connect( s_get("iface3_proc0"), s_get("iface3_proc7") )	# 1356
	#sess.connect( s_get("iface3_proc0"), s_get("iface3_proc8") )	# 0
	#sess.connect( s_get("iface3_proc0"), s_get("iface3_proc9") )	# 0
	#sess.connect( s_get("iface3_proc0"), s_get("iface3_proc10") )	# 140
	sess.connect( s_get("iface3_proc0"), s_get("iface3_proc11") )	# 3496	AV: 10694, 10695
	#sess.connect( s_get("iface3_proc0"), s_get("iface3_proc12") )
	#sess.connect( s_get("iface3_proc0"), s_get("iface3_proc13") )
	#sess.connect( s_get("iface3_proc0"), s_get("iface3_proc14") )
	#sess.connect( s_get("iface3_proc0"), s_get("iface3_proc15") )
	#sess.connect( s_get("iface3_proc0"), s_get("iface3_proc16") )

	with open("audits/iface3_graph.udg", "w+") as o:
		o.write( sess.render_graph_udraw() )

	sess.fuzz()


def iface4(ip, port, **opts):
	global uuid,ver
	uuid = opts['uuid']
	ver = opts['ver']
	aalogger.object_uuid = opts['object_uuid']
	sess = sessions.session( session_filename="audits/aaLogger_iface4_fuzz.session", sleep_time=1, timeout=1 )
	#sess = sessions.session(  )
	target = sessions.target( ip, port )
	
	#target.netmon = sulley.pedrpc.client("127.0.0.1", 26004)
	target.procmon = sulley.pedrpc.client("127.0.0.1", 28001)
	target.procmon_options = {
		"proc_name": "aalogger_patched.exe",
		"stop_commands": ["TERMINATE_PID"],
		"start_commands": ["net start aalogger_patched"]
	}
	aalogger.procmon = target.procmon
	aalogger.session = sess
	target.procmon.set_ifname("iface4")
	
	sess.add_target( target )
	sess.pre_send = rpc_init

	sess.connect( s_get("iface4_proc0") )
	#sess.connect( s_get("iface4_proc0"), s_get("iface4_proc1") )
	#sess.connect( s_get("iface4_proc0"), s_get("iface4_proc2") )
	#sess.connect( s_get("iface4_proc0"), s_get("iface4_proc3") )
	sess.connect( s_get("iface4_proc0"), s_get("iface4_proc4") )
	#sess.connect( s_get("iface4_proc0"), s_get("iface4_proc5") )
	#sess.connect( s_get("iface4_proc0"), s_get("iface4_proc6") )
	#sess.connect( s_get("iface4_proc0"), s_get("iface4_proc7") )
	sess.connect( s_get("iface4_proc0"), s_get("iface4_proc8") )
	sess.connect( s_get("iface4_proc0"), s_get("iface4_proc9") )
	sess.connect( s_get("iface4_proc0"), s_get("iface4_proc10") )
	#sess.connect( s_get("iface4_proc0"), s_get("iface4_proc11") )
	#sess.connect( s_get("iface4_proc0"), s_get("iface4_proc12") )
	#sess.connect( s_get("iface4_proc0"), s_get("iface4_proc13") )
	#sess.connect( s_get("iface4_proc0"), s_get("iface4_proc14") )
	sess.connect( s_get("iface4_proc0"), s_get("iface4_proc15") )
	sess.connect( s_get("iface4_proc0"), s_get("iface4_proc16") )

	with open("audits/iface4_graph.udg", "w+") as o:
		o.write( sess.render_graph_udraw() )

	sess.fuzz()


def iface5(ip, port, **opts):
	global uuid,ver
	uuid = opts['uuid']
	ver = opts['ver']
	aalogger.object_uuid = opts['object_uuid']
	sess = sessions.session( session_filename="audits/aaLogger_iface5_fuzz.session", sleep_time=1, timeout=1 )
	#sess = sessions.session(  )
	target = sessions.target( ip, port )
	
	#target.netmon = sulley.pedrpc.client("127.0.0.1", 26005)
	target.procmon = sulley.pedrpc.client("127.0.0.1", 28001)
	target.procmon_options = {
		"proc_name": "aalogger_patched.exe",
		"stop_commands": ["TERMINATE_PID"],
		"start_commands": ["net start aalogger_patched"]
	}
	aalogger.procmon = target.procmon
	aalogger.session = sess
	target.procmon.set_ifname("iface5")
	
	sess.add_target( target )
	sess.pre_send = rpc_init

	sess.connect( s_get("iface5_proc0") )
	#sess.connect( s_get("iface5_proc0"), s_get("iface5_proc1") )
	#sess.connect( s_get("iface5_proc0"), s_get("iface5_proc2") )
	#sess.connect( s_get("iface5_proc0"), s_get("iface5_proc3") )
	#sess.connect( s_get("iface5_proc0"), s_get("iface5_proc4") )
	#sess.connect( s_get("iface5_proc0"), s_get("iface5_proc5") )
	#sess.connect( s_get("iface5_proc0"), s_get("iface5_proc6") )
	#sess.connect( s_get("iface5_proc0"), s_get("iface5_proc7") )
	#sess.connect( s_get("iface5_proc0"), s_get("iface5_proc8") )
	#sess.connect( s_get("iface5_proc0"), s_get("iface5_proc9") )
	#sess.connect( s_get("iface5_proc0"), s_get("iface5_proc10") )
	#sess.connect( s_get("iface5_proc0"), s_get("iface5_proc11") )
	#sess.connect( s_get("iface5_proc0"), s_get("iface5_proc12") )
	#sess.connect( s_get("iface5_proc0"), s_get("iface5_proc13") )
	sess.connect( s_get("iface5_proc0"), s_get("iface5_proc14") )
	#sess.connect( s_get("iface5_proc0"), s_get("iface5_proc15") )
	#sess.connect( s_get("iface5_proc0"), s_get("iface5_proc16") )

	with open("audits/iface5_graph.udg", "w+") as o:
		o.write( sess.render_graph_udraw() )

	sess.fuzz()


def iface6(ip, port, **opts):
	global uuid,ver
	uuid = opts['uuid']
	ver = opts['ver']
	aalogger.object_uuid = opts['object_uuid']
	sess = sessions.session( session_filename="audits/aaLogger_iface6_fuzz.session", sleep_time=1, timeout=1 )
	#sess = sessions.session(  )
	target = sessions.target( ip, port )
	
	#target.netmon = sulley.pedrpc.client("127.0.0.1", 26006)
	target.procmon = sulley.pedrpc.client("127.0.0.1", 28001)
	target.procmon_options = {
		"proc_name": "aalogger_patched.exe",
		"stop_commands": ["TERMINATE_PID"],
		"start_commands": ["net start aalogger_patched"]
	}
	aalogger.procmon = target.procmon
	aalogger.session = sess
	target.procmon.set_ifname("iface6")
	
	sess.add_target( target )
	sess.pre_send = rpc_init

	sess.connect( s_get("iface6_proc0") )
	sess.connect( s_get("iface6_proc0"), s_get("iface6_proc1") )
	sess.connect( s_get("iface6_proc0"), s_get("iface6_proc2") )
	sess.connect( s_get("iface6_proc0"), s_get("iface6_proc3") )
	sess.connect( s_get("iface6_proc0"), s_get("iface6_proc4") )
	sess.connect( s_get("iface6_proc0"), s_get("iface6_proc5") ) 	# arbitrary folder create
	
	with open("audits/iface6_graph.udg", "w+") as o:
		o.write( sess.render_graph_udraw() )

	sess.fuzz()


def iface7(ip, port, **opts):
	global uuid,ver
	uuid = opts['uuid']
	ver = opts['ver']
	aalogger.object_uuid = opts['object_uuid']
	sess = sessions.session( session_filename="audits/aaLogger_iface7_fuzz.session", sleep_time=1, timeout=1 )
	#sess = sessions.session(  )
	target = sessions.target( ip, port )
	
	#target.netmon = sulley.pedrpc.client("127.0.0.1", 26007)
	target.procmon = sulley.pedrpc.client("127.0.0.1", 28001)
	target.procmon_options = {
		"proc_name": "aalogger_patched.exe",
		"stop_commands": ["TERMINATE_PID"],
		"start_commands": ["net start aalogger_patched"]
	}
	aalogger.procmon = target.procmon
	aalogger.session = sess
	target.procmon.set_ifname("iface7")

	sess.add_target( target )
	sess.pre_send = rpc_init

	sess.connect( s_get("iface7_proc0") )
	sess.connect( s_get("iface7_proc0"), s_get("iface7_proc1") )
	sess.connect( s_get("iface7_proc0"), s_get("iface7_proc2") )
	sess.connect( s_get("iface7_proc0"), s_get("iface7_proc3") )
	sess.connect( s_get("iface7_proc0"), s_get("iface7_proc4") )
	sess.connect( s_get("iface7_proc0"), s_get("iface7_proc5") )
	sess.connect( s_get("iface7_proc0"), s_get("iface7_proc6") )
	sess.connect( s_get("iface7_proc0"), s_get("iface7_proc7") )
	sess.connect( s_get("iface7_proc0"), s_get("iface7_proc8") )
	sess.connect( s_get("iface7_proc0"), s_get("iface7_proc9") )

	with open("audits/iface7_graph.udg", "w+") as o:
		o.write( sess.render_graph_udraw() )

	sess.fuzz()

def iface8(ip, port, **opts):
	global uuid,ver
	uuid = opts['uuid']
	ver = opts['ver']
	aalogger.object_uuid = opts['object_uuid']
	sess = sessions.session( session_filename="audits/aaLogger_iface8_fuzz.session", sleep_time=1, timeout=1 )
	#sess = sessions.session(  )
	target = sessions.target( ip, port )
	
	#target.netmon = sulley.pedrpc.client("127.0.0.1", 26008)
	target.procmon = sulley.pedrpc.client("127.0.0.1", 28001)
	target.procmon_options = {
		"proc_name": "aalogger_patched.exe",
		"stop_commands": ["TERMINATE_PID"],
		"start_commands": ["net start aalogger_patched"]
	}
	aalogger.procmon = target.procmon
	aalogger.session = sess
	target.procmon.set_ifname("iface8")
	
	sess.add_target( target )
	sess.pre_send = rpc_init

	sess.connect( s_get("iface8_proc0") )
	sess.connect( s_get("iface8_proc0"), s_get("iface8_proc1") )
	sess.connect( s_get("iface8_proc0"), s_get("iface8_proc2") )
	sess.connect( s_get("iface8_proc0"), s_get("iface8_proc3") )
	sess.connect( s_get("iface8_proc0"), s_get("iface8_proc4") )
	sess.connect( s_get("iface8_proc0"), s_get("iface8_proc5") )
	sess.connect( s_get("iface8_proc0"), s_get("iface8_proc6") )
	sess.connect( s_get("iface8_proc0"), s_get("iface8_proc7") )
	sess.connect( s_get("iface8_proc0"), s_get("iface8_proc8") )
	sess.connect( s_get("iface8_proc0"), s_get("iface8_proc9") )
	sess.connect( s_get("iface8_proc0"), s_get("iface8_proc10") )
	
	with open("audits/iface8_graph.udg", "w+") as o:
		o.write( sess.render_graph_udraw() )

	sess.fuzz()



#IP = "192.168.27.30"
#PORT = 4748
IP = "127.0.0.1"
PORT = 59014
ifaces = {
#	iface1: {"uuid": "1981974b-6bf7-46cb-9640-0260bbb551ba", "object_uuid": "85289e8c-f262-4797-84df-3e4ba60efe8b"},
#	iface2: {"uuid": "2e7064d9-1c16-4d79-bf70-ff99be73a87f", "object_uuid": "2cdd8e9d-7183-4900-a818-6a75b3eec6f6"},
	iface3: {"uuid": "ea3669c2-3bde-4cc1-b34a-77708ce6b37c", "object_uuid": "f50e2ac7-23df-47ec-858b-20c9eefdbf61"},
	#iface4: {"uuid": "57810394-0d55-4e58-a04c-d71ab05575d6", "object_uuid": "c8a6bc84-7d25-44cb-8794-72b1d571a419"},
	#iface5: {"uuid": "65d6a0c8-7e7b-4c9b-ba42-801d23640739", "object_uuid": "e9ed30b5-faac-4b31-a540-0ee7b2787d3e"},
	#iface6: {"uuid": "1bd1e783-1074-49ed-964e-0b2fa71561d7", "object_uuid": "edd3a8ca-9376-4522-bbc9-f97b529dac83"},
	#iface7: {"uuid": "9cf211ad-548c-46c2-ab9f-991f637ec8b9", "object_uuid": "002d23b8-0e28-47b3-819c-979cfa0b78ed"},
	#iface8: {"uuid": "f2a0d0a2-8a56-4ec2-9c0f-b5fe49b668a8", "object_uuid": "7abb9d07-ed51-4bd1-beee-3f7337f7e1e8"}
}
if __name__ == '__main__':
	for (iface,opts) in ifaces.items():
		iface( ip=IP, port=PORT, uuid=opts["uuid"], ver="1.0", object_uuid=opts["object_uuid"] )

