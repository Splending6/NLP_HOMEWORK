# 获取符号字典列表

import platform as plat

def GetSymbolList(datapath):
	'''
	加载拼音符号列表，用于标记符号
	返回一个列表list类型变量
	'''
	if(datapath != ''):
		if(datapath[-1]!='/' or datapath[-1]!='\\'):
			datapath = datapath + '/'
	
	txt_obj=open(datapath + 'dict.txt','r',encoding='UTF-8')
	txt_text=txt_obj.read()
	txt_lines=txt_text.split('\n')
	list_symbol=[]
	for i in txt_lines:
		if(i!=''):
			txt_l=i.split('\t')
			list_symbol.append(txt_l[0])
	txt_obj.close()
	list_symbol.append('_')
	#SymbolNum = len(list_symbol)
	return list_symbol
	
def GetSymbolList_trash(datapath):
	'''
	加载拼音符号列表，用于标记符号
	返回一个列表list类型变量
	'''

	datapath_ = datapath.strip('dataset\\') + '\\'
	
	txt_obj=open(datapath_ + 'dict.txt','r',encoding='UTF-8')
	txt_text=txt_obj.read()        
	txt_lines=txt_text.split('\n')
	list_symbol=[]
	for i in txt_lines:
		if(i!=''):
			txt_l=i.split('\t')						
			list_symbol.append(txt_l[0])            
	txt_obj.close()
	list_symbol.append('_')
	#SymbolNum = len(list_symbol)
	return list_symbol

if(__name__ == '__main__'):
	GetSymbolList('./abc/')