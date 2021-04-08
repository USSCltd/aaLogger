from sulley import *
import struct
import random
import datetime

object_uuid = ''
opnum = 0
procmon = object()
session = object()

def log_query(filename, data):
	if len(data) > 1000000:
		return
	with open(filename, "wb") as f:
		f.write(data)

def rpc_request_encoder0(data):
	print "[debug] request opnum:0"
	procmon.set_opnum(0)
	data = utils.dcerpc.request( object_uuid, 0, data )
	log_query( "audits/requests/request_op0_%d_%s.bin" % (session.total_mutant_index, datetime.datetime.now().strftime("%H-%M-%S") ), data )
	return data

def rpc_request_encoder1(data):
	print "[debug] request opnum:1"
	procmon.set_opnum(1)
	data = utils.dcerpc.request( object_uuid, 1, data )
	log_query( "audits/requests/request_op1_%d_%s.bin" % (session.total_mutant_index, datetime.datetime.now().strftime("%H-%M-%S") ), data )
	return data

def rpc_request_encoder2(data):
	print "[debug] request opnum:2"
	procmon.set_opnum(2)
	data = utils.dcerpc.request( object_uuid, 2, data )
	log_query( "audits/requests/request_op2_%d_%s.bin" % (session.total_mutant_index, datetime.datetime.now().strftime("%H-%M-%S") ), data )
	return data

def rpc_request_encoder3(data):
	print "[debug] request opnum:3"
	procmon.set_opnum(3)
	data = utils.dcerpc.request( object_uuid, 3, data )
	log_query( "audits/requests/request_op3_%d_%s.bin" % ( session.total_mutant_index, datetime.datetime.now().strftime("%H-%M-%S") ), data )
	return data

def rpc_request_encoder4(data):
	print "[debug] request opnum:4"
	procmon.set_opnum(4)
	data = utils.dcerpc.request( object_uuid, 4, data )
	log_query( "audits/requests/request_op4_%d_%s.bin" % ( session.total_mutant_index, datetime.datetime.now().strftime("%H-%M-%S") ), data )
	return data

def rpc_request_encoder5(data):
	print "[debug] request opnum:5"
	procmon.set_opnum(5)
	data = utils.dcerpc.request( object_uuid, 5, data )
	log_query( "audits/requests/request_op5_%d_%s.bin" % ( session.total_mutant_index, datetime.datetime.now().strftime("%H-%M-%S") ), data )
	return data

def rpc_request_encoder6(data):
	print "[debug] request opnum:6"
	procmon.set_opnum(6)
	data = utils.dcerpc.request( object_uuid, 6, data )
	log_query( "audits/requests/request_op6_%d_%s.bin" % ( session.total_mutant_index, datetime.datetime.now().strftime("%H-%M-%S") ), data )
	return data

def rpc_request_encoder7(data):
	print "[debug] request opnum:7"
	procmon.set_opnum(7)
	data = utils.dcerpc.request( object_uuid, 7, data )
	log_query( "audits/requests/request_op7_%d_%s.bin" % ( session.total_mutant_index, datetime.datetime.now().strftime("%H-%M-%S") ), data )
	return data

def rpc_request_encoder8(data):
	print "[debug] request opnum:8"
	procmon.set_opnum(8)
	data = utils.dcerpc.request( object_uuid, 8, data )
	log_query( "audits/requests/request_op8_%d_%s.bin" % ( session.total_mutant_index, datetime.datetime.now().strftime("%H-%M-%S") ), data )
	return data

def rpc_request_encoder9(data):
	print "[debug] request opnum:9"
	procmon.set_opnum(9)
	data = utils.dcerpc.request( object_uuid, 9, data )
	log_query( "audits/requests/request_op9_%d_%s.bin" % ( session.total_mutant_index, datetime.datetime.now().strftime("%H-%M-%S") ), data )
	return data

def rpc_request_encoder10(data):
	print "[debug] request opnum:10"
	procmon.set_opnum(10)
	data = utils.dcerpc.request( object_uuid, 10, data )
	log_query( "audits/requests/request_op10_%d_%s.bin" % ( session.total_mutant_index, datetime.datetime.now().strftime("%H-%M-%S") ), data )
	return data

def rpc_request_encoder11(data):
	print "[debug] request opnum:11"
	procmon.set_opnum(11)
	data = utils.dcerpc.request( object_uuid, 11, data )
	log_query( "audits/requests/request_op11_%d_%s.bin" % ( session.total_mutant_index, datetime.datetime.now().strftime("%H-%M-%S") ), data )
	return data

def rpc_request_encoder12(data):
	print "[debug] request opnum:12"
	procmon.set_opnum(12)
	data = utils.dcerpc.request( object_uuid, 12, data )
	log_query( "audits/requests/request_op12_%d_%s.bin" % ( session.total_mutant_index, datetime.datetime.now().strftime("%H-%M-%S") ), data )
	return data

def rpc_request_encoder13(data):
	print "[debug] request opnum:13"
	procmon.set_opnum(13)
	data = utils.dcerpc.request( object_uuid, 13, data )
	log_query( "audits/requests/request_op13_%d_%s.bin" % ( session.total_mutant_index, datetime.datetime.now().strftime("%H-%M-%S") ), data )
	return data

def rpc_request_encoder14(data):
	print "[debug] request opnum:14"
	procmon.set_opnum(14)
	data = utils.dcerpc.request( object_uuid, 14, data )
	log_query( "audits/requests/request_op14_%d_%s.bin" % ( session.total_mutant_index, datetime.datetime.now().strftime("%H-%M-%S") ), data )
	return data

def rpc_request_encoder15(data):
	print "[debug] request opnum:15"
	procmon.set_opnum(15)
	data = utils.dcerpc.request( object_uuid, 15, data )
	log_query( "audits/requests/request_op15_%d_%s.bin" % ( session.total_mutant_index, datetime.datetime.now().strftime("%H-%M-%S") ), data )
	return data

def rpc_request_encoder16(data):
	print "[debug] request opnum:16"
	procmon.set_opnum(16)
	data = utils.dcerpc.request( object_uuid, 16, data )
	log_query( "audits/requests/request_op16_%d_%s.bin" % ( session.total_mutant_index, datetime.datetime.now().strftime("%H-%M-%S") ) , data )
	return data


def string_len(data):
	return struct.pack( "<I", len(data) )

def wstring_len(data):
	return struct.pack( "<I", len(data) / 2 )

def array_len(data):
	return struct.pack( "<I", len(data) / 4 )

def string_pad(data):
	return "\x00" * ( (4 - len(data)) % 4 )

def wstring_pad(data):
	return "\x00\x00" if (len(data)/2) % 2 else ""

def array_repeat_iface3(_):
	s_get("iface3_proc5").names["string3"].render()
	data = s_get("iface3_proc5").names["string3"].rendered
	return ''.join( ( struct.pack('<I', random.random() * 0xffffffff) for _ in xrange( len(data) ) ) ) or "NOTDATA"

def array_repeat_iface4(_):
	s_get("iface4_proc5").names["string3"].render()
	data = s_get("iface4_proc5").names["string3"].rendered
	return ''.join( ( struct.pack('<I', random.random() * 0xffffffff) for _ in xrange( len(data) ) ) ) or "NOTDATA"

def array_repeat_iface5(_):
	s_get("iface5_proc5").names["string3"].render()
	data = s_get("iface5_proc5").names["string3"].rendered
	return ''.join( ( struct.pack('<I', random.random() * 0xffffffff) for _ in xrange( len(data) ) ) ) or "NOTDATA"


''' UUID 1 1981974b-6bf7-46cb-9640-0260bbb551ba'''

s_initialize( "iface1_proc0" )
if s_block_start( "do", encoder=rpc_request_encoder0 ):
	#[in] context_handle arg0
	s_static( "\x88", name="context_handle" )
	
	#[in, string] wchar_t * arg1
	s_checksum("string", algorithm=wstring_len)
	s_static("\x00\x00\x00\x00")
	s_checksum("string", algorithm=wstring_len)
	if s_block_start("string"):
		s_string("wm", name="arg1", encoding="utf_16_le", fuzzable=True)
		s_static("\x00\x00")
	s_block_end()
	
	s_checksum("string", name="pad1", algorithm=wstring_pad)

	#[in] int arg2
	s_dword(-1, format="binary", endian="<", fuzzable=True)
s_block_end()

s_initialize("iface1_proc1")
if s_block_start("do", encoder=rpc_request_encoder1):
	#[in] context_handle arg0
	s_static("\x88", name="context_handle")

	#[in, string] wchar_t * arg1
	s_checksum("string", algorithm=wstring_len)
	s_static("\x00\x00\x00\x00")
	s_checksum("string", algorithm=wstring_len)
	if s_block_start("string"):
		s_string("wm", name="arg1", encoding="utf_16_le", fuzzable=True)
		s_static("\x00\x00")
	s_block_end()
s_block_end()

s_initialize("iface1_proc2")
if s_block_start("do", encoder=rpc_request_encoder2):
	#[in] context_handle arg0
	s_static("\x88", name="context_handle")

	#[out, string] wchar_t * arg1
	s_checksum("string", algorithm=wstring_len)
	s_static("\x00\x00\x00\x00")
	s_checksum("string", algorithm=wstring_len)
	if s_block_start("string"):
		s_string("wm", name="arg1", encoding="utf_16_le", fuzzable=True)
		s_static("\x00\x00")
	s_block_end()
s_block_end()

s_initialize("iface1_proc3")
if s_block_start("do", encoder=rpc_request_encoder3):
	#[in] context_handle arg0
	s_static("\x88", name="context_handle")

	#[in, unique] wchar_t * arg1
	s_static("\x00\x00\x02\x00")
	s_checksum("string", algorithm=wstring_len)
	s_static("\x00\x00\x00\x00")
	s_checksum("string", algorithm=wstring_len)
	if s_block_start("string"):
		s_string("wm", name="arg1", encoding="utf_16_le", fuzzable=True)
		s_static("\x00\x00")
	s_block_end()

	s_checksum("string", name="pad1", algorithm=wstring_pad)

	#[in, string] wchar_t * arg2
	s_checksum("string2", algorithm=wstring_len)
	s_static("\x00\x00\x00\x00")
	s_checksum("string2", algorithm=wstring_len)
	if s_block_start("string2"):
		s_string("wm", name="arg2", encoding="utf_16_le", fuzzable=True)
		s_static("\x00\x00")
	s_block_end()

	#[out] wchar_t[32]
s_block_end()

s_initialize("iface1_proc4")
if s_block_start("do", encoder=rpc_request_encoder4):
	#[in] context_handle arg0
	s_static("\x88", name="context_handle")

	#[in, unique] wchar_t * arg1
	s_static("\x00\x00\x02\x00")
	s_checksum("string1", algorithm=wstring_len)
	s_static("\x00\x00\x00\x00")
	s_checksum("string1", algorithm=wstring_len)
	if s_block_start("string1"):
		s_string("wm", name="arg1", encoding="utf_16_le", fuzzable=False)
		s_static("\x00\x00")
	s_block_end()

	s_checksum("string1", name="pad1", algorithm=wstring_pad)

	#[in, string] wchar_t * arg2
	s_checksum("string2", algorithm=wstring_len)
	s_static("\x00\x00\x00\x00")
	s_checksum("string2", algorithm=wstring_len)
	if s_block_start("string2"):
		s_string("wm", name="arg2", encoding="utf_16_le", fuzzable=True)
		s_static("\x00\x00")
	s_block_end()

	s_checksum("string2", name="pad2", algorithm=wstring_pad)

	#[in] int arg3
	s_dword(-1, format="binary", endian="<", fuzzable=True)

	#[out] wchar_t[32]
s_block_end()

s_initialize( "iface1_proc5" )
if s_block_start( "do", encoder=rpc_request_encoder5 ):
	#[in] context_handle arg0
	s_static( "\x88", name="context_handle" )
	
	#[in] int arg1
	s_dword(-1, format="binary", endian="<", fuzzable=True)

	#[in, string] wchar_t * arg2
	s_checksum("string1", algorithm=wstring_len)
	s_static("\x00\x00\x00\x00")
	s_checksum("string1", algorithm=wstring_len)
	if s_block_start("string1"):
		s_string("wm", encoding="utf_16_le", fuzzable=True)
		s_static("\x00\x00")
	s_block_end()
	
	s_checksum("string1", name="pad1", algorithm=wstring_pad)

	#[in] int arg3
	s_dword(-1, format="binary", endian="<", fuzzable=True)

	#[in, string, unique] wchar_t * arg4
	s_static("\x00\x00\x02\x00")
	s_checksum("string2", algorithm=wstring_len)
	s_static("\x00\x00\x00\x00")
	s_checksum("string2", algorithm=wstring_len)
	if s_block_start("string2"):
		s_string("wm", encoding="utf_16_le", fuzzable=True)
		s_static("\x00\x00")
	s_block_end()

	s_checksum("string2", name="pad2", algorithm=wstring_pad)

	#[in, string] wchar_t * arg5
	s_checksum("string3", algorithm=wstring_len)
	s_static("\x00\x00\x00\x00")
	s_checksum("string3", algorithm=wstring_len)
	if s_block_start("string3"):
		s_string("wm", encoding="utf_16_le", fuzzable=True)
		s_static("\x00\x00")
	s_block_end()
s_block_end()

s_initialize( "iface1_proc6" )
# not fuzzable



''' UUID 2 2e7064d9-1c16-4d79-bf70-ff99be73a87f '''

s_initialize( "iface2_proc0" )
if s_block_start("do", encoder=rpc_request_encoder0):
	#[in] context_handle arg0
	s_static( "\x88", name="context_handle" )

	#[in, string] wchar_t * arg1
	s_checksum("string1", algorithm=wstring_len)
	s_static("\x00\x00\x00\x00")
	s_checksum("string1", algorithm=wstring_len)
	if s_block_start("string1"):
		s_string("wm", encoding="utf_16_le", fuzzable=True)
		s_static("\x00\x00")
	s_block_end()
s_block_end()

s_initialize( "iface2_proc1" )
if s_block_start("do", encoder=rpc_request_encoder1):
	#[in] context_handle arg0
	s_static( "\x88", name="context_handle" )
	
	s_static("\x00\x00\x00\x00")
	#[in] double arg1
	s_qword(-1, format="binary", endian="<", fuzzable=True)

	#[in] double arg2
	s_qword(-1, format="binary", endian="<", fuzzable=True)

	#[in, string] wchar_t * arg3
	s_checksum("string1", algorithm=wstring_len)
	s_static("\x00\x00\x00\x00")
	s_checksum("string1", algorithm=wstring_len)
	if s_block_start("string1"):
		s_string("wm", encoding="utf_16_le", fuzzable=True)
		s_static("\x00\x00")
	s_block_end()
s_block_end()

s_initialize("iface2_proc2")
if s_block_start("do", encoder=rpc_request_encoder2):
	#[in] context_handle arg0
	s_static("\x88", name="context_handle")

	#[in] int arg1
	s_dword(-1, format="binary", endian="<", fuzzable=True)
s_block_end()



''' UUID 3 ea3669c2-3bde-4cc1-b34a-77708ce6b37c '''

s_initialize("iface3_proc0")
if s_block_start("do", encoder=rpc_request_encoder0):
	#[in] context_handle arg0
	s_static("\x88", name="context_handle")

	#[in] int arg1
	s_word(-1, format="binary", fuzzable=False)

	s_static("\x00\x00")
	#[in] int arg2
	s_dword(2756, format="binary", endian="<", fuzzable=False)
s_block_end()


s_initialize("iface3_proc1")
if s_block_start("do", encoder=rpc_request_encoder1):
	#[in] context_handle arg0
	s_static("\x88", name="context_handle")

	#[out] wchar_t[]

	#[in] int arg1
	s_dword(-1, format="binary", endian="<", fuzzable=True)
s_block_end()


s_initialize("iface3_proc2")
if s_block_start("do", encoder=rpc_request_encoder2):
	#[in] context_handle arg0
	s_static("\x88", name="context_handle")

	#[in] int arg1
	s_word(-1, format="binary", fuzzable=True)
s_block_end()


s_initialize("iface3_proc3")
if s_block_start("do", encoder=rpc_request_encoder3):
	#[in] context_handle arg0
	s_static("\x88", name="context_handle")

	#[in] int arg1
	s_dword(1, format="binary", endian="<", fuzzable=True)

	#[in] int arg2
	s_dword(1, format="binary", endian="<", fuzzable=False)

	#[out] wchar_t[32]

	#[in_out] int * arg3
	s_dword(1, format="binary", endian="<", fuzzable=False)

	#[out] wchar_t[2]

	s_static("\x00\x00")
	#[in] short arg4
	s_word(1, format="binary", endian="<", fuzzable=False)
s_block_end()


s_initialize( "iface3_proc4" )
# not fuzzable

s_initialize( "iface3_proc5" )
if s_block_start("do", encoder=rpc_request_encoder5):
	#[in] context_handle arg0
	s_static("\x88", name="context_handle")
	
	s_static("\x00\x00\x00\x00")
	#[in] hyper arg1
	s_qword(-1, format="binary", fuzzable=True)
	
	#[in] hyper arg2
	s_qword(-1, format="binary", fuzzable=False)

	#[in] int arg3
	s_checksum("string1", algorithm=string_len)

	#[in][size_is(arg3)] char_t[*] arg4
	s_checksum("string1", algorithm=string_len)
	if s_block_start("string1"):
		s_string("wm", encoding="ascii", fuzzable=False)
		s_static("\x00")
	s_block_end()

	s_checksum("string1", algorithm=string_pad)
	
	
	#[in] int arg5
	s_checksum("string3", algorithm=string_len)

	#[in][size_is(arg5)] FC_LONG[*] arg6
	s_checksum("string3", algorithm=string_len)
	if s_block_start("string2", encoder=array_repeat_iface3):
		s_static("VOID")
	s_block_end()

	s_checksum("string2", algorithm=wstring_pad)

	#[in][size_is(arg5)] char_t[*] arg7
	s_checksum("string3", algorithm=string_len)
	if s_block_start("string3"):
		s_string("WM", encoding="ascii", fuzzable=False)
		s_static("\x00")
	s_block_end()

	s_checksum("string3", algorithm=string_pad)
	
	
	#[in] int arg8
	s_checksum("string4", algorithm=array_len)

	#[in][size_is(arg8)] FC_LONG[*] arg9
	s_checksum("string4", algorithm=array_len)
	if s_block_start("string4"):
		s_random("\x00\x00\x00\x00", min_length=4, max_length=256, step=4, fuzzable=False)
	s_block_end()

	s_checksum("string4", algorithm=wstring_pad)


	#[in] int arg10
	s_checksum("string5", algorithm=array_len)

	#[in][size_is(arg10)] FC_LONG[*] arg11
	s_checksum("string5", algorithm=array_len)
	if s_block_start("string5"):
		s_random("\x00\x00\x00\x00", min_length=4, max_length=256, step=4, fuzzable=False)
	s_block_end()

	s_checksum("string5", algorithm=wstring_pad)

	#[in] int arg12
	s_checksum("string6", algorithm=wstring_len)

	#[in][size_is(arg12)] wchar_t[*] arg13
	s_checksum("string6", algorithm=wstring_len)
	if s_block_start("string6"):
		s_string("wm", encoding="utf_16_le", fuzzable=False)
		s_static("\x00\x00")
	s_block_end()

	s_checksum("string6", algorithm=wstring_pad)

	#[in] int arg14
	s_checksum("string7", algorithm=wstring_len)

	#[in][size_is(arg14)] wchar_t[*] arg15
	s_checksum("string7", algorithm=wstring_len)
	if s_block_start("string7"):
		s_string("wm", encoding="utf_16_le", fuzzable=False)
		s_static("\x00\x00")
	s_block_end()

	s_checksum("string7", algorithm=wstring_pad)

	#[in] int arg16
	s_checksum("string8", algorithm=wstring_len)

	#[in][size_is(arg16)] wchar_t[*] arg17
	s_checksum("string8", algorithm=wstring_len)
	if s_block_start("string8"):
		s_string("wm", encoding="utf_16_le", fuzzable=False)
		s_static("\x00\x00")
	s_block_end()

	s_checksum("string8", algorithm=wstring_pad)
	
	#[in] hyper arg18
	s_qword(-1, format="binary", fuzzable=False)

s_block_end()

s_initialize("iface3_proc6")
if s_block_start("do", encoder=rpc_request_encoder6):
	#[in] context_handle arg0
	s_static("\x88", name="context_handle")

	s_static("\x00\x00\x00\x00")
	#[in] hyper arg1
	s_qword(-1, format="binary", fuzzable=True)
s_block_end()


s_initialize("iface3_proc7")
if s_block_start("do", encoder=rpc_request_encoder7):
	#[in] context_handle arg0
	s_static("\x88", name="context_handle")

	#[in] arg1 wchar_t[2]
	s_checksum("string1", algorithm=wstring_len)
	s_static("\x00\x00\x00\x00")
	s_checksum("string1", algorithm=wstring_len)
	if s_block_start("string1"):
		s_string("wm", encoding="utf_16_le", fuzzable=True)
		s_static("\x00\x00")
	s_block_end()

	s_checksum("string1", name="pad1", algorithm=wstring_pad)

	#[in] int arg2
	s_dword(-1, format="binary", endian="<", fuzzable=False)

	#[in] int arg3
	s_dword(-1, format="binary", endian="<", fuzzable=False)
s_block_end()


s_initialize( "iface3_proc8" )
# not fuzzable

s_initialize( "iface3_proc9" )
# not fuzzable


s_initialize("iface3_proc10")
if s_block_start("do", encoder=rpc_request_encoder10):
	#[in] context_handle arg0
	s_static("\x88", name="context_handle")

	s_static("\x00\x00\x00\x00")
	#[in] hyper arg1
	s_qword(-1, format="binary", fuzzable=True)
s_block_end()


s_initialize("iface3_proc11")
if s_block_start("do", encoder=rpc_request_encoder11):
	s_static("\x88", name="context_handle")

	#[in] int arg1
	s_dword(1, format="binary", endian="<", fuzzable=False)	# HEAP SPRAY

	#[in] int arg2
	s_checksum("string1", algorithm=array_len)

	#[in][size_is(arg2)] FC_LONG[*] arg3
	s_checksum("string1", algorithm=array_len)
	if s_block_start("string1"):
		s_random("\x00\x00\x00\x00", min_length=4, max_length=256, step=4, fuzzable=True)
	s_block_end()

	s_checksum("string1", algorithm=wstring_pad)

	#[in] int arg4
	s_checksum("string2", algorithm=array_len)

	#[in][size_is(arg4)] FC_LONG[*] arg5
	s_checksum("string2", algorithm=array_len)
	if s_block_start("string2"):
		s_random("\x00\x00\x00\x00", min_length=4, max_length=256, step=4, fuzzable=True)
	s_block_end()

	s_checksum("string2", algorithm=wstring_pad)

	#[in] int arg6
	s_checksum("string3", algorithm=wstring_len)

	#[in][size_is(arg6)] wchar_t[*] arg7
	s_checksum("string3", algorithm=wstring_len)
	if s_block_start("string3"):
		s_string("wm", encoding="utf_16_le", fuzzable=True)
		s_static("\x00\x00")
	s_block_end()

	s_checksum("string3", algorithm=wstring_pad)

	#[in] int arg8
	s_checksum("string4", algorithm=wstring_len)

	#[in][size_is(arg8)] wchar_t[*] arg9
	s_checksum("string4", algorithm=wstring_len)
	if s_block_start("string4"):
		s_string("wm", encoding="utf_16_le", fuzzable=True)
		s_static("\x00\x00")
	s_block_end()

	s_checksum("string4", algorithm=wstring_pad)

	#[in] int arg10
	s_checksum("string5", algorithm=wstring_len)

	#[in][size_is(arg10)] wchar_t[*] arg11
	s_checksum("string5", algorithm=wstring_len)
	if s_block_start("string5"):
		s_string("wm", encoding="utf_16_le", fuzzable=True)
		s_static("\x00\x00")
	s_block_end()

	s_checksum("string5", algorithm=wstring_pad)

	#[in] int arg12
	s_dword(-1, format="binary", endian="<", fuzzable=True)
s_block_end()


s_initialize("iface3_proc12")
if s_block_start("do", encoder=rpc_request_encoder12):
	#[in] context_handle arg0
	s_static("\x88", name="context_handle")

	#[in] int arg1
	s_dword(-1, format="binary", fuzzable=True)
s_block_end()


s_initialize("iface3_proc13")
if s_block_start("do", encoder=rpc_request_encoder13):
	#[in] context_handle arg0
	s_static("\x88", name="context_handle")

	s_static("\x00\x00\x00\x00")
	#[in] hyper arg1
	s_qword(-1, format="binary", fuzzable=True)

	#[in] int arg2
	s_dword(-1, format="binary", fuzzable=False)
s_block_end()


s_initialize("iface3_proc14")
if s_block_start("do", encoder=rpc_request_encoder14):
	#[in] context_handle arg0
	s_static("\x88", name="context_handle")

	#[in] arg1 wchar_t[4]
	s_checksum("string1", algorithm=wstring_len)
	s_static("\x00\x00\x00\x00")
	s_checksum("string1", algorithm=wstring_len)
	if s_block_start("string1"):
		s_string("wm", encoding="utf_16_le", fuzzable=True)
		s_static("\x00\x00")
	s_block_end()

	s_checksum("string1", algorithm=wstring_pad)
	
	#[in] int arg2
	s_dword(-1, format="binary", fuzzable=False)

	#[in] int arg3
	s_dword(-1, format="binary", fuzzable=False)

	#[in] int arg4
	s_dword(-1, format="binary", fuzzable=False)

	#[in] wchar_t[4] arg5
	s_checksum("string2", algorithm=wstring_len)
	s_static("\x00\x00\x00\x00")
	s_checksum("string2", algorithm=wstring_len)
	if s_block_start("string2"):
		s_string("wm", encoding="utf_16_le", fuzzable=False)
		s_static("\x00\x00")
	s_block_end()

	#s_checksum("string1", algorithm=wstring_pad)
s_block_end()


s_initialize("iface3_proc15")
# not fuzzable

s_initialize("iface3_proc16")
# not fuzzable



''' UUID 4 57810394-0d55-4e58-a04c-d71ab05575d6 '''

s_initialize("iface4_proc0")
if s_block_start("do", encoder=rpc_request_encoder0):
	#[in] context_handle arg0
	s_static("\x88", name="context_handle")

	#[in] int arg1
	s_word(-1, format="binary", fuzzable=False)

	s_static("\x00\x00")
	#[in] int arg2
	s_dword(2756, format="binary", endian="<", fuzzable=False)
s_block_end()


s_initialize("iface4_proc1")
if s_block_start("do", encoder=rpc_request_encoder1):
	#[in] context_handle arg0
	s_static("\x88", name="context_handle")

	#[out] wchar_t[]

	#[in] int arg1
	s_dword(-1, format="binary", endian="<", fuzzable=True)
s_block_end()


s_initialize("iface4_proc2")
if s_block_start("do", encoder=rpc_request_encoder2):
	#[in] context_handle arg0
	s_static("\x88", name="context_handle")

	#[in] short arg1
	s_word(-1, format="binary", fuzzable=True)

	#[in] short arg2
	s_word(-1, format="binary", fuzzable=True)
s_block_end()


s_initialize("iface4_proc3")
if s_block_start("do", encoder=rpc_request_encoder3):
	#[in] context_handle arg0
	s_static("\x88", name="context_handle")

	#[in] int arg1
	s_dword(1, format="binary", endian="<", fuzzable=True)

	#[in] int arg2
	s_dword(1, format="binary", endian="<", fuzzable=True)

	#[out] wchar_t[32]

	#[in_out] int * arg3
	s_dword(1, format="binary", endian="<", fuzzable=True)

	#[out] wchar_t[2]

	s_static("\x00\x00")
	#[in] short arg4
	s_word(1, format="binary", endian="<", fuzzable=True)
s_block_end()


s_initialize( "iface4_proc4" )
# not fuzzable

s_initialize( "iface4_proc5" )
if s_block_start("do", encoder=rpc_request_encoder5):
	#[in] context_handle arg0
	s_static("\x88", name="context_handle")
	
	s_static("\x00\x00\x00\x00")
	#[in] hyper arg1
	s_qword(-1, format="binary", fuzzable=True)
	
	#[in] hyper arg2
	s_qword(-1, format="binary", fuzzable=True)

	#[in] int arg3
	s_checksum("string1", algorithm=string_len)

	#[in][size_is(arg3)] char_t[*] arg4
	s_checksum("string1", algorithm=string_len)
	if s_block_start("string1"):
		s_string("wm", encoding="ascii", fuzzable=True)
		s_static("\x00")
	s_block_end()

	s_checksum("string1", algorithm=string_pad)
	
	
	#[in] int arg5
	s_checksum("string3", algorithm=string_len)

	#[in][size_is(arg5)] FC_LONG[*] arg6
	s_checksum("string3", algorithm=string_len)
	if s_block_start("string2", encoder=array_repeat_iface4):
		s_static("VOID")
	s_block_end()

	s_checksum("string2", algorithm=wstring_pad)

	#[in][size_is(arg5)] char_t[*] arg7
	s_checksum("string3", algorithm=string_len)
	if s_block_start("string3"):
		s_string("WM", encoding="ascii", fuzzable=True)
		s_static("\x00")
	s_block_end()

	s_checksum("string3", algorithm=string_pad)
	
	
	#[in] int arg8
	s_checksum("string4", algorithm=array_len)

	#[in][size_is(arg8)] FC_LONG[*] arg9
	s_checksum("string4", algorithm=array_len)
	if s_block_start("string4"):
		s_random("\x00\x00\x00\x00", min_length=4, max_length=256, step=4)
	s_block_end()

	s_checksum("string4", algorithm=wstring_pad)


	#[in] int arg10
	s_checksum("string5", algorithm=array_len)

	#[in][size_is(arg10)] FC_LONG[*] arg11
	s_checksum("string5", algorithm=array_len)
	if s_block_start("string5"):
		s_random("\x00\x00\x00\x00", min_length=4, max_length=256, step=4)
	s_block_end()

	s_checksum("string5", algorithm=wstring_pad)

	#[in] int arg12
	s_checksum("string6", algorithm=wstring_len)

	#[in][size_is(arg12)] wchar_t[*] arg13
	s_checksum("string6", algorithm=wstring_len)
	if s_block_start("string6"):
		s_string("wm", encoding="utf_16_le", fuzzable=True)
		s_static("\x00\x00")
	s_block_end()

	s_checksum("string6", algorithm=wstring_pad)

	#[in] int arg14
	s_checksum("string7", algorithm=wstring_len)

	#[in][size_is(arg14)] wchar_t[*] arg15
	s_checksum("string7", algorithm=wstring_len)
	if s_block_start("string7"):
		s_string("wm", encoding="utf_16_le", fuzzable=True)
		s_static("\x00\x00")
	s_block_end()

	s_checksum("string7", algorithm=wstring_pad)

	#[in] int arg16
	s_checksum("string8", algorithm=wstring_len)

	#[in][size_is(arg16)] wchar_t[*] arg17
	s_checksum("string8", algorithm=wstring_len)
	if s_block_start("string8"):
		s_string("wm", encoding="utf_16_le", fuzzable=True)
		s_static("\x00\x00")
	s_block_end()

	s_checksum("string8", algorithm=wstring_pad)
	
	#[in] hyper arg18
	s_qword(-1, format="binary", fuzzable=True)

s_block_end()

s_initialize("iface4_proc6")
if s_block_start("do", encoder=rpc_request_encoder6):
	#[in] context_handle arg0
	s_static("\x88", name="context_handle")

	s_static("\x00\x00\x00\x00")
	#[in] hyper arg1
	s_qword(-1, format="binary", fuzzable=True)
s_block_end()


s_initialize("iface4_proc7")
if s_block_start("do", encoder=rpc_request_encoder7):
	#[in] context_handle arg0
	s_static("\x88", name="context_handle")

	#[in] arg1 wchar_t[2]
	s_checksum("string1", algorithm=wstring_len)
	s_static("\x00\x00\x00\x00")
	s_checksum("string1", algorithm=wstring_len)
	if s_block_start("string1"):
		s_string("wm", encoding="utf_16_le", fuzzable=True)
		s_static("\x00\x00")
	s_block_end()

	s_checksum("string1", name="pad1", algorithm=wstring_pad)

	#[in] int arg2
	s_dword(-1, format="binary", endian="<", fuzzable=True)

	#[in] int arg3
	s_dword(-1, format="binary", endian="<", fuzzable=True)
s_block_end()


s_initialize( "iface4_proc8" )
# not fuzzable

s_initialize( "iface4_proc9" )
# not fuzzable


s_initialize("iface4_proc10")
if s_block_start("do", encoder=rpc_request_encoder10):
	#[in] context_handle arg0
	s_static("\x88", name="context_handle")

	s_static("\x00\x00\x00\x00")
	#[in] hyper arg1
	s_qword(-1, format="binary", fuzzable=True)
s_block_end()


s_initialize("iface4_proc11")
if s_block_start("do", encoder=rpc_request_encoder11):
	s_static("\x88", name="context_handle")

	#[in] int arg1
	s_dword(1, format="binary", endian="<", fuzzable=False)

	#[in] int arg2
	s_checksum("string1", algorithm=array_len)

	#[in][size_is(arg2)] FC_LONG[*] arg3
	s_checksum("string1", algorithm=array_len)
	if s_block_start("string1"):
		s_random("\x00\x00\x00\x00", min_length=4, max_length=256, step=4)
	s_block_end()

	s_checksum("string1", algorithm=wstring_pad)

	#[in] int arg4
	s_checksum("string2", algorithm=array_len)

	#[in][size_is(arg4)] FC_LONG[*] arg5
	s_checksum("string2", algorithm=array_len)
	if s_block_start("string2"):
		s_random("\x00\x00\x00\x00", min_length=4, max_length=256, step=4)
	s_block_end()

	s_checksum("string2", algorithm=wstring_pad)

	#[in] int arg6
	s_checksum("string3", algorithm=wstring_len)

	#[in][size_is(arg6)] wchar_t[*] arg7
	s_checksum("string3", algorithm=wstring_len)
	if s_block_start("string3"):
		s_string("wm", encoding="utf_16_le", fuzzable=True)
		s_static("\x00\x00")
	s_block_end()

	s_checksum("string3", algorithm=wstring_pad)

	#[in] int arg8
	s_checksum("string4", algorithm=wstring_len)

	#[in][size_is(arg8)] wchar_t[*] arg9
	s_checksum("string4", algorithm=wstring_len)
	if s_block_start("string4"):
		s_string("wm", encoding="utf_16_le", fuzzable=True)
		s_static("\x00\x00")
	s_block_end()

	s_checksum("string4", algorithm=wstring_pad)

	#[in] int arg10
	s_checksum("string5", algorithm=wstring_len)

	#[in][size_is(arg10)] wchar_t[*] arg11
	s_checksum("string5", algorithm=wstring_len)
	if s_block_start("string5"):
		s_string("wm", encoding="utf_16_le", fuzzable=True)
		s_static("\x00\x00")
	s_block_end()

	s_checksum("string5", algorithm=wstring_pad)

	#[in] int arg12
	s_dword(-1, format="binary", endian="<", fuzzable=True)
s_block_end()


s_initialize("iface4_proc12")
if s_block_start("do", encoder=rpc_request_encoder12):
	#[in] context_handle arg0
	s_static("\x88", name="context_handle")

	#[in] int arg1
	s_dword(-1, format="binary", fuzzable=True)
s_block_end()


s_initialize("iface4_proc13")
if s_block_start("do", encoder=rpc_request_encoder13):
	#[in] context_handle arg0
	s_static("\x88", name="context_handle")

	s_static("\x00\x00\x00\x00")
	#[in] hyper arg1
	s_qword(-1, format="binary", fuzzable=True)

	#[in] int arg2
	s_dword(-1, format="binary", fuzzable=True)
s_block_end()


s_initialize("iface4_proc14")
if s_block_start("do", encoder=rpc_request_encoder14):
	#[in] context_handle arg0
	s_static("\x88", name="context_handle")

	#[in] arg1 wchar_t[4]
	s_checksum("string1", algorithm=wstring_len)
	s_static("\x00\x00\x00\x00")
	s_checksum("string1", algorithm=wstring_len)
	if s_block_start("string1"):
		s_string("wm", encoding="utf_16_le", fuzzable=True)
		s_static("\x00\x00")
	s_block_end()

	s_checksum("string1", algorithm=wstring_pad)
	
	#[in] int arg2
	s_dword(-1, format="binary", fuzzable=True)

	#[in] int arg3
	s_dword(-1, format="binary", fuzzable=True)

	#[in] int arg4
	s_dword(-1, format="binary", fuzzable=True)

	#[in] wchar_t[4] arg5
	s_checksum("string2", algorithm=wstring_len)
	s_static("\x00\x00\x00\x00")
	s_checksum("string2", algorithm=wstring_len)
	if s_block_start("string2"):
		s_string("wm", encoding="utf_16_le", fuzzable=True)
		s_static("\x00\x00")
	s_block_end()

	#s_checksum("string1", algorithm=wstring_pad)
s_block_end()


s_initialize("iface4_proc15")
# not fuzzable

s_initialize("iface4_proc16")
# not fuzzable


''' UUID 5 65d6a0c8-7e7b-4c9b-ba42-801d23640739 '''

s_initialize("iface5_proc0")
if s_block_start("do", encoder=rpc_request_encoder0):
	#[in] context_handle arg0
	s_static("\x88", name="context_handle")

	#[in] int arg1
	s_word(-1, format="binary", fuzzable=False)

	s_static("\x00\x00")
	#[in] int arg2
	s_dword(2756, format="binary", endian="<", fuzzable=False)
s_block_end()


s_initialize("iface5_proc1")
if s_block_start("do", encoder=rpc_request_encoder1):
	#[in] context_handle arg0
	s_static("\x88", name="context_handle")

	#[out] wchar_t[]

	#[in] int arg1
	s_dword(-1, format="binary", endian="<", fuzzable=True)
s_block_end()


s_initialize("iface5_proc2")
if s_block_start("do", encoder=rpc_request_encoder2):
	#[in] context_handle arg0
	s_static("\x88", name="context_handle")

	#[in] short arg1
	s_word(-1, format="binary", fuzzable=True)

	#[in] short arg2
	s_word(-1, format="binary", fuzzable=True)
s_block_end()


s_initialize("iface5_proc3")
if s_block_start("do", encoder=rpc_request_encoder3):
	#[in] context_handle arg0
	s_static("\x88", name="context_handle")

	#[in] int arg1
	s_dword(1, format="binary", endian="<", fuzzable=True)

	#[in] int arg2
	s_dword(1, format="binary", endian="<", fuzzable=True)

	#[out] wchar_t[32]

	#[in_out] int * arg3
	s_dword(1, format="binary", endian="<", fuzzable=True)

	#[out] wchar_t[2]

	s_static("\x00\x00")
	#[in] short arg4
	s_word(1, format="binary", endian="<", fuzzable=True)
s_block_end()


s_initialize( "iface5_proc4" )
# not fuzzable

s_initialize( "iface5_proc5" )
if s_block_start("do", encoder=rpc_request_encoder5):
	#[in] context_handle arg0
	s_static("\x88", name="context_handle")
	
	s_static("\x00\x00\x00\x00")
	#[in] hyper arg1
	s_qword(-1, format="binary", fuzzable=True)
	
	#[in] hyper arg2
	s_qword(-1, format="binary", fuzzable=True)

	#[in] int arg3
	s_checksum("string1", algorithm=string_len)

	#[in][size_is(arg3)] char_t[*] arg4
	s_checksum("string1", algorithm=string_len)
	if s_block_start("string1"):
		s_string("wm", encoding="ascii", fuzzable=True)
		s_static("\x00")
	s_block_end()

	s_checksum("string1", algorithm=string_pad)
	
	
	#[in] int arg5
	s_checksum("string3", algorithm=string_len)

	#[in][size_is(arg5)] FC_LONG[*] arg6
	s_checksum("string3", algorithm=string_len)
	if s_block_start("string2", encoder=array_repeat_iface5):
		s_static("VOID")
	s_block_end()

	s_checksum("string2", algorithm=wstring_pad)

	#[in][size_is(arg5)] char_t[*] arg7
	s_checksum("string3", algorithm=string_len)
	if s_block_start("string3"):
		s_string("WM", encoding="ascii", fuzzable=True)
		s_static("\x00")
	s_block_end()

	s_checksum("string3", algorithm=string_pad)
	
	
	#[in] int arg8
	s_checksum("string4", algorithm=array_len)

	#[in][size_is(arg8)] FC_LONG[*] arg9
	s_checksum("string4", algorithm=array_len)
	if s_block_start("string4"):
		s_random("\x00\x00\x00\x00", min_length=4, max_length=256, step=4)
	s_block_end()

	s_checksum("string4", algorithm=wstring_pad)


	#[in] int arg10
	s_checksum("string5", algorithm=array_len)

	#[in][size_is(arg10)] FC_LONG[*] arg11
	s_checksum("string5", algorithm=array_len)
	if s_block_start("string5"):
		s_random("\x00\x00\x00\x00", min_length=4, max_length=256, step=4)
	s_block_end()

	s_checksum("string5", algorithm=wstring_pad)

	#[in] int arg12
	s_checksum("string6", algorithm=wstring_len)

	#[in][size_is(arg12)] wchar_t[*] arg13
	s_checksum("string6", algorithm=wstring_len)
	if s_block_start("string6"):
		s_string("wm", encoding="utf_16_le", fuzzable=True)
		s_static("\x00\x00")
	s_block_end()

	s_checksum("string6", algorithm=wstring_pad)

	#[in] int arg14
	s_checksum("string7", algorithm=wstring_len)

	#[in][size_is(arg14)] wchar_t[*] arg15
	s_checksum("string7", algorithm=wstring_len)
	if s_block_start("string7"):
		s_string("wm", encoding="utf_16_le", fuzzable=True)
		s_static("\x00\x00")
	s_block_end()

	s_checksum("string7", algorithm=wstring_pad)

	#[in] int arg16
	s_checksum("string8", algorithm=wstring_len)

	#[in][size_is(arg16)] wchar_t[*] arg17
	s_checksum("string8", algorithm=wstring_len)
	if s_block_start("string8"):
		s_string("wm", encoding="utf_16_le", fuzzable=True)
		s_static("\x00\x00")
	s_block_end()

	s_checksum("string8", algorithm=wstring_pad)
	
	#[in] hyper arg18
	s_qword(-1, format="binary", fuzzable=True)

s_block_end()

s_initialize("iface5_proc6")
if s_block_start("do", encoder=rpc_request_encoder6):
	#[in] context_handle arg0
	s_static("\x88", name="context_handle")

	s_static("\x00\x00\x00\x00")
	#[in] hyper arg1
	s_qword(-1, format="binary", fuzzable=True)
s_block_end()


s_initialize("iface5_proc7")
if s_block_start("do", encoder=rpc_request_encoder7):
	#[in] context_handle arg0
	s_static("\x88", name="context_handle")

	#[in] arg1 wchar_t[2]
	s_checksum("string1", algorithm=wstring_len)
	s_static("\x00\x00\x00\x00")
	s_checksum("string1", algorithm=wstring_len)
	if s_block_start("string1"):
		s_string("wm", encoding="utf_16_le", fuzzable=True)
		s_static("\x00\x00")
	s_block_end()

	s_checksum("string1", name="pad1", algorithm=wstring_pad)

	#[in] int arg2
	s_dword(-1, format="binary", endian="<", fuzzable=True)

	#[in] int arg3
	s_dword(-1, format="binary", endian="<", fuzzable=True)
s_block_end()


s_initialize( "iface5_proc8" )
# not fuzzable

s_initialize( "iface5_proc9" )
# not fuzzable


s_initialize("iface5_proc10")
if s_block_start("do", encoder=rpc_request_encoder10):
	#[in] context_handle arg0
	s_static("\x88", name="context_handle")

	s_static("\x00\x00\x00\x00")
	#[in] hyper arg1
	s_qword(-1, format="binary", fuzzable=True)
s_block_end()


s_initialize("iface5_proc11")
if s_block_start("do", encoder=rpc_request_encoder11):
	s_static("\x88", name="context_handle")

	#[in] int arg1
	s_dword(1, format="binary", endian="<", fuzzable=False)

	#[in] int arg2
	s_checksum("string1", algorithm=array_len)

	#[in][size_is(arg2)] FC_LONG[*] arg3
	s_checksum("string1", algorithm=array_len)
	if s_block_start("string1"):
		s_random("\x00\x00\x00\x00", min_length=4, max_length=256, step=4)
	s_block_end()

	s_checksum("string1", algorithm=wstring_pad)

	#[in] int arg4
	s_checksum("string2", algorithm=array_len)

	#[in][size_is(arg4)] FC_LONG[*] arg5
	s_checksum("string2", algorithm=array_len)
	if s_block_start("string2"):
		s_random("\x00\x00\x00\x00", min_length=4, max_length=256, step=4)
	s_block_end()

	s_checksum("string2", algorithm=wstring_pad)

	#[in] int arg6
	s_checksum("string3", algorithm=wstring_len)

	#[in][size_is(arg6)] wchar_t[*] arg7
	s_checksum("string3", algorithm=wstring_len)
	if s_block_start("string3"):
		s_string("wm", encoding="utf_16_le", fuzzable=True)
		s_static("\x00\x00")
	s_block_end()

	s_checksum("string3", algorithm=wstring_pad)

	#[in] int arg8
	s_checksum("string4", algorithm=wstring_len)

	#[in][size_is(arg8)] wchar_t[*] arg9
	s_checksum("string4", algorithm=wstring_len)
	if s_block_start("string4"):
		s_string("wm", encoding="utf_16_le", fuzzable=True)
		s_static("\x00\x00")
	s_block_end()

	s_checksum("string4", algorithm=wstring_pad)

	#[in] int arg10
	s_checksum("string5", algorithm=wstring_len)

	#[in][size_is(arg10)] wchar_t[*] arg11
	s_checksum("string5", algorithm=wstring_len)
	if s_block_start("string5"):
		s_string("wm", encoding="utf_16_le", fuzzable=True)
		s_static("\x00\x00")
	s_block_end()

	s_checksum("string5", algorithm=wstring_pad)

	#[in] int arg12
	s_dword(-1, format="binary", endian="<", fuzzable=True)
s_block_end()


s_initialize("iface5_proc12")
if s_block_start("do", encoder=rpc_request_encoder12):
	#[in] context_handle arg0
	s_static("\x88", name="context_handle")

	#[in] int arg1
	s_dword(-1, format="binary", fuzzable=True)
s_block_end()


s_initialize("iface5_proc13")
if s_block_start("do", encoder=rpc_request_encoder13):
	#[in] context_handle arg0
	s_static("\x88", name="context_handle")

	s_static("\x00\x00\x00\x00")
	#[in] hyper arg1
	s_qword(-1, format="binary", fuzzable=True)

	#[in] int arg2
	s_dword(-1, format="binary", fuzzable=True)
s_block_end()


s_initialize("iface5_proc14")
if s_block_start("do", encoder=rpc_request_encoder14):
	#[in] context_handle arg0
	s_static("\x88", name="context_handle")

	#[in] arg1 wchar_t[4]
	s_checksum("string1", algorithm=wstring_len)
	s_static("\x00\x00\x00\x00")
	s_checksum("string1", algorithm=wstring_len)
	if s_block_start("string1"):
		s_string("wm", encoding="utf_16_le", fuzzable=True)
		s_static("\x00\x00")
	s_block_end()

	s_checksum("string1", algorithm=wstring_pad)
	
	#[in] int arg2
	s_dword(-1, format="binary", fuzzable=True)

	#[in] int arg3
	s_dword(-1, format="binary", fuzzable=True)

	#[in] int arg4
	s_dword(-1, format="binary", fuzzable=True)

	#[in] wchar_t[4] arg5
	s_checksum("string2", algorithm=wstring_len)
	s_static("\x00\x00\x00\x00")
	s_checksum("string2", algorithm=wstring_len)
	if s_block_start("string2"):
		s_string("wm", encoding="utf_16_le", fuzzable=True)
		s_static("\x00\x00")
	s_block_end()

	#s_checksum("string1", algorithm=wstring_pad)
s_block_end()


s_initialize("iface5_proc15")
# not fuzzable

s_initialize("iface5_proc16")
# not fuzzable


''' UUID 6 1bd1e783-1074-49ed-964e-0b2fa71561d7 '''

s_initialize("iface6_proc0")
# not fuzzable

s_initialize("iface6_proc1")
# not fuzzable

s_initialize("iface6_proc2")
if s_block_start("do", encoder=rpc_request_encoder2):
	#[in] context_handle arg0
	s_static("\x88", name="context_handle")

	#[in] int arg1
	s_dword(-1, format="binary", fuzzable=True)
s_block_end()


s_initialize("iface6_proc3")
if s_block_start("do", encoder=rpc_request_encoder3):
	#[in] context_handle arg0
	s_static("\x88", name="context_handle")

	#[in] int arg1
	s_dword(-1, format="binary", fuzzable=True)
s_block_end()


s_initialize("iface6_proc4")
if s_block_start("do", encoder=rpc_request_encoder4):
	#[in] context_handle arg0
	s_static("\x88", name="context_handle")

	#[out] wchar_t[]
	#[in] int arg1
	s_dword(-1, format="binary", fuzzable=True)
s_block_end()


s_initialize("iface6_proc5")
if s_block_start("do", encoder=rpc_request_encoder5):
	#[in] context_handle arg0
	s_static("\x88", name="context_handle")

	#[in] wchar_t[] arg1
	s_checksum("string1", algorithm=wstring_len)
	s_static("\x00\x00\x00\x00")
	s_checksum("string1", algorithm=wstring_len)
	if s_block_start("string1"):
		s_string("wm", encoding="utf_16_le", fuzzable=True)
		s_static("\x00\x00")
	s_block_end()

	#s_checksum("string1", algorithm=wstring_pad)
s_block_end()



''' UUID 7 9cf211ad-548c-46c2-ab9f-991f637ec8b9 '''

s_initialize("iface7_proc0")
# not fuzzable

s_initialize("iface7_proc1")
# not fuzzable

s_initialize("iface7_proc2")
if s_block_start("do", encoder=rpc_request_encoder2):
	#[in] context_handle arg0
	s_static("\x88", name="context_handle")

	#[in] int arg1
	s_dword(-1, format="binary", fuzzable=True)
s_block_end()


s_initialize("iface7_proc3")
if s_block_start("do", encoder=rpc_request_encoder3):
	#[in] context_handle arg0
	s_static("\x88", name="context_handle")

	#[in] int arg1
	s_dword(-1, format="binary", fuzzable=True)
s_block_end()


s_initialize("iface7_proc4")
if s_block_start("do", encoder=rpc_request_encoder4):
	#[in] context_handle arg0
	s_static("\x88", name="context_handle")

	#[out] wchar_t[]
	#[in] int arg1
	s_dword(-1, format="binary", fuzzable=True)
s_block_end()


s_initialize("iface7_proc5")
if s_block_start("do", encoder=rpc_request_encoder5):
	#[in] context_handle arg0
	s_static("\x88", name="context_handle")

	#[in] wchar_t[] arg1
	s_checksum("string1", algorithm=wstring_len)
	s_static("\x00\x00\x00\x00")
	s_checksum("string1", algorithm=wstring_len)
	if s_block_start("string1"):
		s_string("wm", encoding="utf_16_le", fuzzable=True)
		s_static("\x00\x00")
	s_block_end()

	#s_checksum("string1", algorithm=wstring_pad)
s_block_end()

s_initialize("iface7_proc6")
# not fuzzable

s_initialize("iface7_proc7")
if s_block_start("do", encoder=rpc_request_encoder7):
	#[in] context_handle arg0
	s_static("\x88", name="context_handle")

	#[in] short arg1
	s_word(-1, format="binary", fuzzable=True)
s_block_end()

s_initialize("iface7_proc8")
if s_block_start("do", encoder=rpc_request_encoder8):
	#[in] context_handle arg0
	s_static("\x88", name="context_handle")

	#[in] wchar_t[] arg1
	s_checksum("string1", algorithm=wstring_len)
	s_static("\x00\x00\x00\x00")
	s_checksum("string1", algorithm=wstring_len)
	if s_block_start("string1"):
		s_string("wm", encoding="utf_16_le", fuzzable=True)
		s_static("\x00\x00")
	s_block_end()

	#s_checksum("string1", algorithm=wstring_pad)
s_block_end()

s_initialize("iface7_proc9")
# not fuzzable


''' UUID 8 f2a0d0a2-8a56-4ec2-9c0f-b5fe49b668a8 '''

s_initialize("iface8_proc0")
# not fuzzable

s_initialize("iface8_proc1")
# not fuzzable

s_initialize("iface8_proc2")
if s_block_start("do", encoder=rpc_request_encoder2):
	#[in] context_handle arg0
	s_static("\x88", name="context_handle")

	#[in] int arg1
	s_checksum("string1", algorithm=wstring_len)

	#[in] arg2 wchar_t[4]
	s_checksum("string1", algorithm=wstring_len)
	if s_block_start("string1"):
		s_string("wm", encoding="utf_16_le", fuzzable=True)
		s_static("\x00\x00")
	s_block_end()
s_block_end()

s_initialize("iface8_proc3")
if s_block_start("do", encoder=rpc_request_encoder3):
	#[in] context_handle arg0
	s_static("\x88", name="context_handle")

	#s_static("\x00\x00")	pad ?
	#[in] int arg1
	s_checksum("string1", algorithm=wstring_len)

	#[in][size_is(arg1)] arg2 wchar_t[*]
	s_checksum("string1", algorithm=wstring_len)
	if s_block_start("string1"):
		s_string("wm", encoding="utf_16_le", fuzzable=True)
		s_static("\x00\x00")
	s_block_end()

s_block_end()

# ???
s_initialize("iface8_proc4")
# ???

# ???
s_initialize("iface8_proc5")
# ???

s_initialize("iface8_proc6")
# not fuzzable

# ???
s_initialize("iface8_proc7")
# ???

# ???
s_initialize("iface8_proc8")
if s_block_start("do", encoder=rpc_request_encoder8):
	#[in] context_handle arg0
	s_static("\x88", name="context_handle")

	#s_static("\x00\x00")
	#[in] int arg1
	s_checksum("string1", algorithm=wstring_len)

	#[in][size_is(arg1)] arg2 wchar_t[*]
	s_checksum("string1", algorithm=wstring_len)
	if s_block_start("string1"):
		s_string("wm", encoding="utf_16_le", fuzzable=True)
		s_static("\x00\x00")
	s_block_end()

	#s_checksum("string1", algorithm=wstring_pad)

	#[in] int arg3
	s_dword(-1, format="binary", endian="<", fuzzable=True)
s_block_end()

s_initialize("iface8_proc9")
# not fuzzable

s_initialize("iface8_proc10")
# not fuzzable