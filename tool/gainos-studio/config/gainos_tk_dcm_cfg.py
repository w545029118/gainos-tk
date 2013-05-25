# -*- coding: utf-8 -*-

"""
/* Copyright 2012, Fan Wang(Parai). All rights reserved.
 *
 * This file is part of GaInOS-Studio.
 */
"""
import xml.etree.ElementTree as ET
from Common import *
class DcmGeneral():
    def __init__(self):
        self.DevErrorDetection = True;
        self.VersionInfoApi   = False;
        self.RespondAllRequest = True;
        self.MainFunctionPeriod = 10; #ms
        self.ResponsePending = True;
        self.MaxNegativeResponse = 10;
        self.MaxNumberofSimultaneousPeriodictransmissions = 10;
        self.PeriodicTransmissionSlow = 10;
        self.PeriodicTransmissionMedium = 11;
        self.PeriodicTransmissionFast = 12;
        self.MaxSourcesforOneDynamicIdentifier = 10;
    def save(self, root):
        nd = ET.Element('General');
        nd.attrib['DevErrorDetection'] = str(self.DevErrorDetection);
        nd.attrib['VersionInfoApi'] = str(self.VersionInfoApi);
        nd.attrib['RespondAllRequest'] = str(self.RespondAllRequest);
        nd.attrib['MainFunctionPeriod'] = str(self.MainFunctionPeriod);
        nd.attrib['ResponsePending'] = str(self.ResponsePending);
        nd.attrib['MaxNegativeResponse'] = str(self.MaxNegativeResponse);
        nd.attrib['MaxNumberofSimultaneousPeriodictransmissions'] = str(self.MaxNumberofSimultaneousPeriodictransmissions);
        nd.attrib['PeriodicTransmissionSlow'] = str(self.PeriodicTransmissionSlow);
        nd.attrib['PeriodicTransmissionMedium'] = str(self.PeriodicTransmissionMedium);
        nd.attrib['PeriodicTransmissionFast'] = str(self.PeriodicTransmissionFast);
        nd.attrib['MaxSourcesforOneDynamicIdentifier'] = str(self.MaxSourcesforOneDynamicIdentifier);
        root.append(nd); 
    def parse(self, nd):
        self.DevErrorDetection = bool(nd.attrib['DevErrorDetection']);
        self.VersionInfoApi = bool(nd.attrib['VersionInfoApi']);
        self.RespondAllRequest = bool(nd.attrib['RespondAllRequest']);
        self.MainFunctionPeriod = int(nd.attrib['MainFunctionPeriod']);
        self.ResponsePending = bool(nd.attrib['ResponsePending']);
        self.MaxNegativeResponse = int(nd.attrib['MaxNegativeResponse']);
        self.MaxNumberofSimultaneousPeriodictransmissions = int(nd.attrib['MaxNumberofSimultaneousPeriodictransmissions']);
        self.PeriodicTransmissionSlow = int(nd.attrib['PeriodicTransmissionSlow']);
        self.PeriodicTransmissionMedium = int(nd.attrib['PeriodicTransmissionMedium']);
        self.PeriodicTransmissionFast = int(nd.attrib['PeriodicTransmissionFast']);
        self.MaxSourcesforOneDynamicIdentifier = int(nd.attrib['MaxSourcesforOneDynamicIdentifier']);

class DcmBuffer():
    def __init__(self, name):
        self.name = name;
        self.size = 8; #bytes
    def save(self, root):
        nd = ET.Element('DcmBuffer');
        nd.attrib['name'] = str(self.name);
        nd.attrib['size'] = str(self.size);
        root.append(nd);
    def parse(self, nd):
        self.name = nd.attrib['name'];
        self.size = int(nd.attrib['size']);
class DcmDidInfoControlAccess():
    def __init__(self, name):
        self.name = name;
        self.DspDidFreezeCurrentState = False;
        self.DspDidFreezeCurrentStateRef = 'NULL';
        self.DspDidResetToDefault = False;
        self.DspDidResetToDefaultRef = 'NULL';
        self.DspDidReturnControlToEcu = False;
        self.DspDidReturnControlToEcuRef = 'NULL';
        self.DspDidShortTermAdjustment = False;
        self.DspDidShortTermAdjustmentRef = 'NULL';
        self.sessionRefList = [];
        self.securityRefList = [];
    def save(self, root):
        nd = ET.Element('DcmDidInfoControlAccess');
        nd.attrib['name'] = str(self.name);
        nd.attrib['DspDidFreezeCurrentState'] = str(self.DspDidFreezeCurrentState);
        nd.attrib['DspDidFreezeCurrentStateRef'] = str(self.DspDidFreezeCurrentStateRef);
        nd.attrib['DspDidResetToDefault'] = str(self.DspDidResetToDefault);
        nd.attrib['DspDidResetToDefaultRef'] = str(self.DspDidResetToDefaultRef);
        nd.attrib['DspDidReturnControlToEcu'] = str(self.DspDidReturnControlToEcu);
        nd.attrib['DspDidReturnControlToEcuRef'] = str(self.DspDidReturnControlToEcuRef);
        nd.attrib['DspDidShortTermAdjustment'] = str(self.DspDidShortTermAdjustment);
        nd.attrib['DspDidShortTermAdjustmentRef'] = str(self.DspDidShortTermAdjustmentRef);
        snd = ET.Element('sessionRefList')
        for ses in self.sessionRefList:
            nd2 = ET.Element('SessionRef')
            nd2.attrib['value'] = str(ses);
            snd.append(nd2);
        nd.append(snd);
        snd = ET.Element('securityRefList')
        for sec in self.securityRefList:
            nd2 = ET.Element('SecurityRef')
            nd2.attrib['value'] = str(sec);
            snd.append(nd2);
        nd.append(snd);
        root.append(nd);
    def parse(self, nd):
        self.name = nd.attrib['name'];
        self.DspDidFreezeCurrentState = bool(nd.attrib['DspDidFreezeCurrentState']);
        self.DspDidFreezeCurrentStateRef = nd.attrib['DspDidFreezeCurrentStateRef'];
        self.DspDidResetToDefault = bool(nd.attrib['DspDidResetToDefault']);
        self.DspDidResetToDefaultRef = nd.attrib['DspDidResetToDefaultRef'];
        self.DspDidReturnControlToEcu = bool(nd.attrib['DspDidReturnControlToEcu']);
        self.DspDidReturnControlToEcuRef = nd.attrib['DspDidReturnControlToEcuRef'];
        self.DspDidShortTermAdjustment = bool(nd.attrib['DspDidShortTermAdjustment']);
        self.DspDidShortTermAdjustmentRef = nd.attrib['DspDidShortTermAdjustmentRef'];
        for nd1 in nd.find('sessionRefList'):
            self.sessionRefList.append(nd1.attrib['value']);
        for nd1 in nd.find('securityRefList'):
            self.securityRefList.append(nd1.attrib['value']);
class  DcmDidInfoReadAccess():
    def __init__(self, name):
        self.name = name;
        self.sessionRefList = [];
        self.securityRefList = [];
    def save(self, root):
        nd = ET.Element('DcmDidInfoControlAccess');
        nd.attrib['name'] = str(self.name);
        snd = ET.Element('sessionRefList')
        for ses in self.sessionRefList:
            nd2 = ET.Element('SessionRef')
            nd2.attrib['value'] = str(ses);
            snd.append(nd2);
        nd.append(snd);
        snd = ET.Element('securityRefList')
        for sec in self.securityRefList:
            nd2 = ET.Element('SecurityRef')
            nd2.attrib['value'] = str(sec);
            snd.append(nd2);
        nd.append(snd);
        root.append(nd);
    def parse(self, nd):
        self.name = nd.attrib['name'];
        for nd1 in nd.find('sessionRefList'):
            self.sessionRefList.append(nd1.attrib['value']);
        for nd1 in nd.find('securityRefList'):
            self.securityRefList.append(nd1.attrib['value']);
class  DcmDidInfoWriteAccess():
    def __init__(self, name):
        self.name = name;
        self.sessionRefList = [];
        self.securityRefList = [];
    def save(self, root):
        nd = ET.Element('DcmDidInfoControlAccess');
        nd.attrib['name'] = str(self.name);
        snd = ET.Element('sessionRefList')
        for ses in self.sessionRefList:
            nd2 = ET.Element('SessionRef')
            nd2.attrib['value'] = str(ses);
            snd.append(nd2);
        nd.append(snd);
        snd = ET.Element('securityRefList')
        for sec in self.securityRefList:
            nd2 = ET.Element('SecurityRef')
            nd2.attrib['value'] = str(sec);
            snd.append(nd2);
        nd.append(snd);
        root.append(nd);
    def parse(self, nd):
        self.name = nd.attrib['name'];
        for nd1 in nd.find('sessionRefList'):
            self.sessionRefList.append(nd1.attrib['value']);
        for nd1 in nd.find('securityRefList'):
            self.securityRefList.append(nd1.attrib['value']);
class DcmDidInfo():
    def __init__(self, name):
        self.name = name;
        self.FixedLength = True;
        self.DynamicllyDefined = False;
        self.ScalingEnable = False;
        self.ScalingInfoSize = 8;
        self.ControlAccessList = [];
        self.ReadAccessList = [];
        self.WriteAccessList = [];
    def save(self, root):
        nd = ET.Element('DcmDidInfo');
        nd.attrib['name'] = str(self.name);
        nd.attrib['FixedLength'] = str(self.FixedLength);
        nd.attrib['DynamicllyDefined'] = str(self.DynamicllyDefined);
        nd.attrib['ScalingEnable'] = str(self.ScalingEnable);
        nd.attrib['ScalingInfoSize'] = str(self.ScalingInfoSize);
        nd2 = ET.Element('ControlAccessList');
        for obj in self.ControlAccessList:
            obj.save(nd2);
        nd.append(nd2);
        nd2 = ET.Element('ReadAccessList');
        for obj in self.ReadAccessList:
            obj.save(nd2);
        nd.append(nd2);
        nd2 = ET.Element('WriteAccessList');
        for obj in self.WriteAccessList:
            obj.save(nd2);
        nd.append(nd2);
        root.append(nd);
    def parse(self, nd):
        self.name = nd.attrib['name'];
        self.FixedLength = bool(nd.attrib['FixedLength']);
        self.DynamicllyDefined = bool(nd.attrib['DynamicllyDefined']);
        self.ScalingEnable = bool(nd.attrib['ScalingEnable']);
        self.ScalingInfoSize = int(nd.attrib['ScalingInfoSize']);
        for nd2 in nd.find('ControlAccessList'):
            obj = DcmDidInfoControlAccess('');
            obj.parse(nd2);
            self.ControlAccessList.append(obj);
        for nd2 in nd.find('ReadAccessList'):
            obj = DcmDidInfoReadAccess('');
            obj.parse(nd2);
            self.ReadAccessList.append(obj);
        for nd2 in nd.find('WriteAccessList'):
            obj = DcmDidInfoWriteAccess('');
            obj.parse(nd2);
            self.WriteAccessList.append(obj);
class DcmDID():
    def __init__(self, name, id):
        self.name = name;
        self.id = id;
        self.size = 64;
        self.didInfoRef = '';
        self.didRef = ''; #I cann't understand 
        self.usePort = False; #for interaction with RTE, not supported now.
        #------ so callback info not configured ...
    def save(self, root):
        nd = ET.Element('DcmDID');
        nd.attrib['name'] = str(self.name);
        nd.attrib['id'] = str(self.id);
        nd.attrib['size'] = str(self.size);
        nd.attrib['didInfoRef'] = str(self.didInfoRef);
        nd.attrib['usePort'] = str(self.usePort);
        root.append(nd);
    def parse(self, nd):
        self.name = nd.attrib['name'];
        self.id = str(nd.attrib['id']);
        self.size = int(nd.attrib['size']);
        self.didInfoRef = str(nd.attrib['didInfoRef']);
        self.usePort = bool(nd.attrib['usePort']);
class DcmRxChannel():
    def __init__(self, name):
        self.name = name;
        self.RxAddrType = 'DCM_PROTOCOL_PHYSICAL_ADDR_TYPE';
        self.RxPdu = ''
    def save(self, root):
        nd  = ET.Element('DcmRxChannel');
        nd.attrib['name'] = str(self.name);
        nd.attrib['RxAddrType'] = str(self.RxAddrType);
        nd.attrib['RxPdu'] = str(self.RxPdu);
        root.append(nd);
    def parse(self, nd):
        self.name = nd.attrib['name'];
        self.RxAddrType = nd.attrib['RxAddrType'];
        self.RxPdu = nd.attrib['RxPdu'];
        
class DcmTxChannel():
    def __init__(self, name):
        self.name = name;
        self.TxPdu = ''
    def save(self, root):
        nd  = ET.Element('DcmTxChannel');
        nd.attrib['name'] = str(self.name);
        nd.attrib['TxPdu'] = str(self.TxPdu);
        root.append(nd)
    def parse(self, nd):
        self.name = nd.attrib['name'];
        self.TxPdu = nd.attrib['TxPdu'];
class DcmConnection():
    def __init__(self, name):
        self.name = name;
        self.RxChannelList = [];
        self.TxChannelList = [];
    def save(self, root):
        nd = ET.Element('DcmConnection');
        nd.attrib['name'] = str(self.name);
        
        nd2 = ET.Element('RxChannelList');
        for obj in self.RxChannelList:
            obj.save(nd2);
        nd.append(nd2);
        
        nd2 = ET.Element('TxChannelList');
        for obj in self.TxChannelList:
            obj.save(nd2);
        nd.append(nd2);
        root.append(nd);
    def parse(self, nd):
        self.name = nd.attrib['name'];
        for nd2 in nd.find('RxChannelList'):
            obj = DcmRxChannel('');
            obj.parse(nd2);
            self.RxChannelList.append(obj);
        for nd2 in nd.find('TxChannelList'):
            obj = DcmTxChannel('');
            obj.parse(nd2);
            self.TxChannelList.append(obj);
class DcmProtocol():
    def __init__(self, name):
        self.name = name;
        self.ProtocolId = 'DCM_UDS_ON_CAN';
        self.TransType = 'DCM_PROTOCOL_TRANS_TYPE_1';
        self.RxBufferID = '';
        self.TxBufferID = '';
        self.TimeLimit = '';
        self.ServiceTable = '';
        self.ConnectionList = [];
    def save(self, root):
        nd = ET.Element('DcmProtocol');
        nd.attrib['name'] = str(self.name);
        nd.attrib['ProtocolId'] = str(self.ProtocolId);
        nd.attrib['TransType'] = str(self.TransType);
        nd.attrib['RxBufferID'] = str(self.RxBufferID);
        nd.attrib['TxBufferID'] = str(self.TxBufferID);
        nd.attrib['TimeLimit'] = str(self.TimeLimit);
        nd.attrib['ServiceTable'] = str(self.ServiceTable);
        nd2 = ET.Element('ConnectionList');
        for obj in self.ConnectionList:
            obj.save(nd2);
        nd.append(nd2);
        root.append(nd);
    def parse(self, nd):
        self.name = str(nd.attrib['name']);
        self.ProtocolId = str(nd.attrib['ProtocolId']);
        self.TransType = str(nd.attrib['TransType']);
        self.RxBufferID = str(nd.attrib['RxBufferID']);
        self.TxBufferID = str(nd.attrib['TxBufferID']);
        self.TimeLimit = str(nd.attrib['TimeLimit']);
        self.ServiceTable = str(nd.attrib['ServiceTable']);
        for nd2 in nd.find('ConnectionList'):
            obj = DcmConnection('')
            obj.parse(nd2);
            self.ConnectionList.append(obj)
class gainos_tk_dcm_obj():
    def __init__(self):
        self.general = DcmGeneral();
        self.bufferList = [];
        self.didInfoList = [];
        self.didList = [];
        self.protocolList = [];
    def save(self, root):
        self.general.save(root);
        
        nd = ET.Element('DcmBufferList');
        for obj in self.bufferList:
            obj.save(nd);
        root.append(nd);
        
        nd = ET.Element('DcmDidInfoList');
        for obj in self.didInfoList:
            obj.save(nd);
        root.append(nd);
        
        nd = ET.Element('DcmDIDList');
        for obj in self.didList:
            obj.save(nd);
        root.append(nd);
        
        nd = ET.Element('DcmProtocolList');
        for obj in self.protocolList:
            obj.save(nd);
        root.append(nd);
        
    def parse(self, root):
        self.general.parse(root.find("General"));
  
        for nd in root.find('DcmBufferList'):
            obj = DcmBuffer('');
            obj.parse(nd);
            self.bufferList.append(obj);

        for nd in root.find('DcmDidInfoList'):
            obj = DcmDidInfo('');
            obj.parse(nd);
            self.didInfoList.append(obj);
            
        for nd in root.find('DcmDIDList'):
            obj = DcmDID('', 0);
            obj.parse(nd);
            self.didList.append(obj);

        for nd in root.find('DcmProtocolList'):
            obj = DcmProtocol('');
            obj.parse(nd);
            self.protocolList.append(obj);
        
class gainos_tk_dcm_cfg():
    def __init__(self, chip=None):
        self.cfg = gainos_tk_dcm_obj();

    def toString(self):
        str='Dcm!\n';
        return str;

    def show(self, title, fileInd, module_list = None):
        from cd_dcm import cd_dcm
        from PyQt4.QtGui import QMessageBox
        depinfo=[];
        md=gcfindModule(module_list, 'EcuC');
        if(md==None):
            QMessageBox(QMessageBox.Information, 'GaInOS Info', 
                'Please Configure EcuC Firstly!').exec_();
            return;
        depinfo.append(md.obj);
        self.dlg  = cd_dcm(title, fileInd, self.cfg, depinfo);
        self.dlg.setModal(False);
        self.dlg.show();
   
    def save(self, root):
        self.cfg.save(root);
    
    def parse(self, root):
        self.cfg.parse(root);

    def gen(self, path):
        return;
  
