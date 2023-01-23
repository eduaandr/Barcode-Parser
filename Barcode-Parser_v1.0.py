# DSS-Monitor
# Description: Program that creates the monitoring points list_device of a digital secondary system
# Authors: Eduardo Andrade
# Date: 2023/01/22
# Version: 2.0

import csv

# creating device class
class device:
    def __init__(self, name, lgos = 1, lsvs = 2, svmd = "sub"):
        self.name = name
        self.lgos = lgos
        self.lsvs = lsvs
        self.svmd = svmd
 
# creating list_device
list_device = []
 
# appending instances to list_device
list_device.append(device('SEL_400G_1', lgos = 5, svmd = "none"))
list_device.append(device('SEL_401_MU', lgos = 1, svmd = "pub"))
list_device.append(device('SEL_411L_2_L', lgos = 2))
list_device.append(device('SEL_411L_2_R', lgos = 2))
list_device.append(device('SEL_421_7_1', lgos = 5, lsvs = 1))
list_device.append(device('SEL_421_7P_L', lgos = 13, svmd = "pub"))
list_device.append(device('SEL_421_7P_R', lgos = 4, svmd = "pub"))
list_device.append(device('SEL_451_6', lgos = 5, lsvs = 1))
list_device.append(device('SEL_487B_2', lgos = 1, lsvs = 4))
list_device.append(device('SEL_487E_5', lgos = 1, lsvs = 4))

class sharedgoose:
    def __init__(self, attr, ttyp):
        self.attr = attr
        self.ttyp = ttyp

class sharedsv:
    def __init__(self, attr, ttyp):
        self.attr = attr
        self.ttyp = ttyp

class sharedptp:
    def __init__(self, attr, ttyp):
        self.attr = attr
        self.ttyp = ttyp

# creating list_vtsharedgoose
list_vtsharedgoose = []
list_vtsharedgoose.append(sharedgoose('Addr', 'STR'))
list_vtsharedgoose.append(sharedgoose('AppID', 'STR'))
list_vtsharedgoose.append(sharedgoose('BufOvflCnt', 'STR'))
list_vtsharedgoose.append(sharedgoose('ConfRev', 'STR'))
list_vtsharedgoose.append(sharedgoose('DatSet', 'STR'))
list_vtsharedgoose.append(sharedgoose('DecErrCnt', 'STR'))
list_vtsharedgoose.append(sharedgoose('ErrSt', 'STR'))
list_vtsharedgoose.append(sharedgoose('GoCBRef', 'STR'))
list_vtsharedgoose.append(sharedgoose('GoID', 'STR'))
list_vtsharedgoose.append(sharedgoose('ID', 'STR'))
list_vtsharedgoose.append(sharedgoose('LastSqNum', 'STR'))
list_vtsharedgoose.append(sharedgoose('LastStNum', 'STR'))
list_vtsharedgoose.append(sharedgoose('MaxDwnTm', 'STR'))
list_vtsharedgoose.append(sharedgoose('MaxMsgLos', 'STR'))
list_vtsharedgoose.append(sharedgoose('MsgLosCnt', 'STR'))
list_vtsharedgoose.append(sharedgoose('NdsCom', 'SPS'))
list_vtsharedgoose.append(sharedgoose('OssCnt', 'STR'))
list_vtsharedgoose.append(sharedgoose('RsStat', 'STR'))
list_vtsharedgoose.append(sharedgoose('RxConfRev', 'STR'))
list_vtsharedgoose.append(sharedgoose('SimSt', 'SPS'))
list_vtsharedgoose.append(sharedgoose('St_', 'SPS'))
list_vtsharedgoose.append(sharedgoose('TalCnt', 'STR'))
list_vtsharedgoose.append(sharedgoose('TotDwnTm', 'STR'))
list_vtsharedgoose.append(sharedgoose('VlanID', 'STR'))
list_vtsharedgoose.append(sharedgoose('VlanPri', 'STR'))

# creating list_vtsharedsv
list_vtsharedsv = []
list_vtsharedsv.append(sharedsv('Addr', 'STR'))
list_vtsharedsv.append(sharedsv('AppID', 'STR'))
list_vtsharedsv.append(sharedsv('ConfRevNum', 'STR'))
list_vtsharedsv.append(sharedsv('DatSet', 'STR'))
list_vtsharedsv.append(sharedsv('DscdCnt', 'STR'))
list_vtsharedsv.append(sharedsv('ErrSt', 'STR'))
list_vtsharedsv.append(sharedsv('ID', 'STR'))
list_vtsharedsv.append(sharedsv('IntpCnt', 'STR'))
list_vtsharedsv.append(sharedsv('MaxDwnTm', 'STR'))
list_vtsharedsv.append(sharedsv('NdsCom', 'SPS'))
list_vtsharedsv.append(sharedsv('NetwDlt', 'STR'))
list_vtsharedsv.append(sharedsv('OosCnt', 'STR'))
list_vtsharedsv.append(sharedsv('RsStat', 'STR'))
list_vtsharedsv.append(sharedsv('RxConfRevNum', 'STR'))
list_vtsharedsv.append(sharedsv('SimSt', 'SPS'))
list_vtsharedsv.append(sharedsv('SmpSynch', 'STR'))
list_vtsharedsv.append(sharedsv('St_', 'SPS'))
list_vtsharedsv.append(sharedsv('SvCBRef', 'STR'))
list_vtsharedsv.append(sharedsv('SvID', 'STR'))
list_vtsharedsv.append(sharedsv('TotDwnTm', 'STR'))
list_vtsharedsv.append(sharedsv('VlanID', 'STR'))
list_vtsharedsv.append(sharedsv('VlanPri', 'STR'))

# creating list_vtsharedptp
list_vtsharedptp = []
list_vtsharedptp.append(sharedptp('ID', 'STR'))
list_vtsharedptp.append(sharedptp('LTIM_TmChgDT', 'STR'))
list_vtsharedptp.append(sharedptp('LTIM_TmChgST', 'STR'))
list_vtsharedptp.append(sharedptp('LTIM_TmDt', 'SPS'))
list_vtsharedptp.append(sharedptp('LTIM_TmOfsTmm', 'STR'))
list_vtsharedptp.append(sharedptp('LTIM_TmUseDT', 'SPS'))
list_vtsharedptp.append(sharedptp('LTMS_St', 'SPS'))
list_vtsharedptp.append(sharedptp('LTMS_TmAcc', 'STR'))
list_vtsharedptp.append(sharedptp('LTMS_TmSrc', 'STR'))
list_vtsharedptp.append(sharedptp('LTMS_TmSrcTyp', 'STR'))
list_vtsharedptp.append(sharedptp('LTMS_TmSyn', 'STR'))
list_vtsharedptp.append(sharedptp('LTMS_TmSynLkd', 'STR'))
list_vtsharedptp.append(sharedptp('LTMS_TmSyn', 'STR'))

def wtvtsharedgoose():
    with open('VT_SHARED_GOOSE.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for obj1 in list_vtsharedgoose:
            writer.writerow(['VT_SHARED_GOOSE.' + str(obj1.attr), obj1.ttyp])

def wtvtsharedsv():
    with open('VT_SHARED_SV.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for obj1 in list_vtsharedsv:
            writer.writerow(['VT_SHARED_SV.' + str(obj1.attr), obj1.ttyp])

def wtvtsharedptp():
    with open('VT_SHARED_PTP.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for obj1 in list_vtsharedptp:
            writer.writerow(['VT_SHARED_PTP.' + str(obj1.attr), obj1.ttyp])

def pgpopulategoose_main():
    file = open(r"PG_POPULATE_GOOSE.txt", "w+")
    flag1 = 1
    for obj1 in list_device:
        for i in range(1, int(obj1.lgos) + 1):
            if flag1 == 1:
                str1 = "IF VT_SELECT_GOOSE." + str(obj1.name) + "_LGOS" + str(i) + ".stVal THEN" + "\n"
                file.write(str1)
                x = pgpopulategoose(obj1.name,i)
                for j in range(0, len(x)):
                    str2 = "\t" + x[j] + "\n"
                    file.write(str2);
                flag1 = 0  
            else:
                str1 = "ELSIF VT_SELECT_GOOSE." + str(obj1.name) + "_LGOS" + str(i) + ".stVal THEN" + "\n"
                file.write(str1)
                x = pgpopulategoose(obj1.name,i)
                for j in range(0, len(x)):
                    str2 = "\t" + x[j] + "\n"
                    file.write(str2);
    file.write("END_IF")
    file.close

def pgpopulategoose(arg1, arg2):
    list1 = []
    name1 = str(arg1) + "_850.CFG." + "LGOS" + str(arg2)
    list1.append("VT_SHARED_GOOSE.St_ := " + str(name1) + ".St_;")
    list1.append("VT_SHARED_GOOSE.ErrSt := ErrSt_GOOSE(" + str(name1) + ".ErrSt);")
    list1.append("VT_SHARED_GOOSE.SimSt := " + str(name1) + ".SimSt;")
    list1.append("VT_SHARED_GOOSE.LastStNum.strVal := DINT_TO_STRING(" + str(name1) + ".LastStNum.stVal);")
    list1.append("VT_SHARED_GOOSE.LastStNum.q := " + str(name1) + ".LastStNum.q;")
    list1.append("VT_SHARED_GOOSE.LastSqNum.strVal := DINT_TO_STRING(" + str(name1) + ".LastSqNum.stVal);")
    list1.append("VT_SHARED_GOOSE.LastSqNum.q := " + str(name1) + ".LastSqNum.q;")
    list1.append("VT_SHARED_GOOSE.ConfRev.strVal := DINT_TO_STRING(" + str(name1) + ".ConfRevNum.stVal);")
    list1.append("VT_SHARED_GOOSE.ConfRev.q := " + str(name1) + ".ConfRevNum.q;")
    list1.append("VT_SHARED_GOOSE.RxConfRev.strVal := DINT_TO_STRING(" + str(name1) + ".RxConfRevNum.stVal);")
    list1.append("VT_SHARED_GOOSE.RxConfRev.q := " + str(name1) + ".RxConfRevNum.q;")
    list1.append("VT_SHARED_GOOSE.NdsCom := " + str(name1) + ".NdsCom;")
    list1.append("VT_SHARED_GOOSE.TotDwnTm.strVal := REAL_TO_STRING(" + str(name1) + ".TotDwnTm.instMag);")
    list1.append("VT_SHARED_GOOSE.TotDwnTm.q := " + str(name1) + ".TotDwnTm.q;")
    list1.append("VT_SHARED_GOOSE.MaxDwnTm.strVal := REAL_TO_STRING(" + str(name1) + ".MaxDwnTm.instMag);")
    list1.append("VT_SHARED_GOOSE.MaxDwnTm.q := " + str(name1) + ".MaxDwnTm.q;")
    list1.append("VT_SHARED_GOOSE.OssCnt.strVal := DINT_TO_STRING(" + str(name1) + ".OosCnt.stVal);")
    list1.append("VT_SHARED_GOOSE.OssCnt.q := " + str(name1) + ".OosCnt.q;")
    list1.append("VT_SHARED_GOOSE.TalCnt.strVal := DINT_TO_STRING(" + str(name1) + ".TalCnt.stVal);")
    list1.append("VT_SHARED_GOOSE.TalCnt.q := " + str(name1) + ".TalCnt.q;")
    list1.append("VT_SHARED_GOOSE.DecErrCnt.strVal := DINT_TO_STRING(" + str(name1) + ".DecErrCnt.stVal);")
    list1.append("VT_SHARED_GOOSE.DecErrCnt.q := " + str(name1) + ".DecErrCnt.q;")
    list1.append("VT_SHARED_GOOSE.BufOvflCnt.strVal := DINT_TO_STRING(" + str(name1) + ".BufOvflCnt.stVal);")
    list1.append("VT_SHARED_GOOSE.BufOvflCnt.q := " + str(name1) + ".BufOvflCnt.q;")
    list1.append("VT_SHARED_GOOSE.MaxMsgLos.strVal := DINT_TO_STRING(" + str(name1) + ".MaxMsgLos.stVal);")
    list1.append("VT_SHARED_GOOSE.MaxMsgLos.q := " + str(name1) + ".MaxMsgLos.q;")
    list1.append("VT_SHARED_GOOSE.MsgLosCnt.strVal := DINT_TO_STRING(" + str(name1) + ".MsgLosCnt.stVal);")
    list1.append("VT_SHARED_GOOSE.MsgLosCnt.q := " + str(name1) + ".MsgLosCnt.q;")
    list1.append("VT_SHARED_GOOSE.RsStat.strVal := TIMESTAMP_TO_STRING(" + str(name1) + ".RsStat.status.t);")
    list1.append("VT_SHARED_GOOSE.RsStat.q := " + str(name1) + ".RsStat.status.q;")
    list1.append(str(name1) + ".RsStat.origin.orCat := orcat_remote_control;")
    list1.append(str(name1) + ".RsStat.operSet := VT_SHARED_GOOSE.RsStat_Cmd.operPulse;")
    list1.append("VT_SHARED_GOOSE.ID.strVal := 'XXXXXXXXXX'; // tag unavailable")                                             # need to review
    list1.append("VT_SHARED_GOOSE.ID.q := VT_SHARED_GOOSE.St_.q; // tag unavailable")                                         # need to review
    list1.append("VT_SHARED_GOOSE.GoCBRef.strVal := 'XXXXXXXXXX'; // tag unavailable")                                        # need to review
    list1.append("VT_SHARED_GOOSE.GoCBRef.q := VT_SHARED_GOOSE.St_.q; // tag unavailable")                                    # need to review
    list1.append("VT_SHARED_GOOSE.DatSet.strVal := 'XXXXXXXXXX'; // tag unavailable")                                         # need to review
    list1.append("VT_SHARED_GOOSE.DatSet.q := VT_SHARED_GOOSE.St_.q; // tag unavailable")                                     # need to review
    list1.append("VT_SHARED_GOOSE.GoID.strVal := 'XXXXXXXXXX'; // tag unavailable")                                           # need to review
    list1.append("VT_SHARED_GOOSE.GoID.q := VT_SHARED_GOOSE.St_.q; // tag unavailable")                                       # need to review
    list1.append("VT_SHARED_GOOSE.Addr.strVal := 'XXXXXXXXXX'; // tag unavailable")                                           # need to review
    list1.append("VT_SHARED_GOOSE.Addr.q := VT_SHARED_GOOSE.St_.q; // tag unavailable")                                       # need to review
    list1.append("VT_SHARED_GOOSE.VlanID.strVal := 'XXXXXXXXXX'; // tag unavailable")                                         # need to review
    list1.append("VT_SHARED_GOOSE.VlanID.q := VT_SHARED_GOOSE.St_.q; // tag unavailable")                                     # need to review
    list1.append("VT_SHARED_GOOSE.VlanPri.strVal := 'XXXXXXXXXX'; // tag unavailable")                                        # need to review
    list1.append("VT_SHARED_GOOSE.VlanPri.q := VT_SHARED_GOOSE.St_.q; // tag unavailable")                                    # need to review
    list1.append("VT_SHARED_GOOSE.AppID.strVal := 'XXXXXXXXXX'; // tag unavailable")                                          # need to review
    list1.append("VT_SHARED_GOOSE.AppID.q := VT_SHARED_GOOSE.St_.q; // tag unavailable")                                      # need to review
    return(list1)

def pgpopulatesv(arg1, arg2):
    list1 = []
    name1 = str(arg1) + "_850.CFG." + "LSVS" + str(arg2)
    list1.append("VT_SHARED_SV.St_ := " + str(name1) + ".St_;")
    list1.append("VT_SHARED_SV.ErrSt := ErrSt_SV(" + str(name1) + ".ErrSt);")
    list1.append("VT_SHARED_SV.SimSt := " + str(name1) + ".SimSt;")
    list1.append("VT_SHARED_SV.Netwdly.strVal := REAL_TO_STRING(" + str(name1) + ".Netwdly.instMag);")
    list1.append("VT_SHARED_SV.Netwdly.q := " + str(name1) + ".Netwdly.q;")
    list1.append("VT_SHARED_SV.SmpSynch := SmpSynch_SV(" + str(name1) + ".SmpSynch);")
    list1.append("VT_SHARED_SV.ConfRevNum.strVal := DINT_TO_STRING(" + str(name1) + ".ConfRevNum.stVal);")
    list1.append("VT_SHARED_SV.ConfRevNum.q := " + str(name1) + ".ConfRevNum.q;")
    list1.append("VT_SHARED_SV.RxConfRevNum.strVal := DINT_TO_STRING(" + str(name1) + ".RxConfRevNum.stVal);")
    list1.append("VT_SHARED_SV.RxConfRevNum.q := " + str(name1) + ".RxConfRevNum.q;")             
    list1.append("VT_SHARED_SV.NdsCom := " + str(name1) + ".NdsCom;")
    list1.append("VT_SHARED_SV.TotDwnTm.strVal := REAL_TO_STRING(" + str(name1) + ".TotDwnTm.instMag);")
    list1.append("VT_SHARED_SV.TotDwnTm.q := " + str(name1) + ".TotDwnTm.q;")             
    list1.append("VT_SHARED_SV.MaxDwnTm.strVal := REAL_TO_STRING(" + str(name1) + ".MaxDwnTm.instMag);")
    list1.append("VT_SHARED_SV.MaxDwnTm.q := " + str(name1) + ".MaxDwnTm.q;")             
    list1.append("VT_SHARED_SV.OosCnt.strVal := DINT_TO_STRING(" + str(name1) + ".OosCnt.stVal);")
    list1.append("VT_SHARED_SV.OosCnt.q := " + str(name1) + ".OosCnt.q;")            
    list1.append("VT_SHARED_SV.DscdCnt.strVal := DINT_TO_STRING(" + str(name1) + ".DscdCnt.stVal);")
    list1.append("VT_SHARED_SV.DscdCnt.q := " + str(name1) + ".DscdCnt.q;")            
    list1.append("VT_SHARED_SV.IntpCnt.strVal := DINT_TO_STRING(" + str(name1) + ".IntpCnt.stVal);")
    list1.append("VT_SHARED_SV.IntpCnt.q := " + str(name1) + ".IntpCnt.q;")            
    list1.append("VT_SHARED_SV.RsStat.strVal := TIMESTAMP_TO_STRING(" + str(name1) + ".RsStat.status.t);")
    list1.append("VT_SHARED_SV.RsStat.q := " + str(name1) + ".RsStat.status.q;")
    list1.append(str(name1) + ".RsStat.origin.orCat := orcat_remote_control;")
    list1.append(str(name1) + ".RsStat.operSet := VT_SHARED_SV.RsStat_Cmd.operPulse;")   
    list1.append("VT_SHARED_SV.ID.strVal := 'XXXXXXXXXX'; // tag unavailable")                                                # need to review
    list1.append("VT_SHARED_SV.ID.q := VT_SHARED_SV.St_.q; // tag unavailable")                                               # need to review
    list1.append("VT_SHARED_SV.SvCBRef.strVal := 'XXXXXXXXXX'; // tag unavailable")                                           # need to review
    list1.append("VT_SHARED_SV.SvCBRef.q := VT_SHARED_SV.St_.q; // tag unavailable")                                          # need to review
    list1.append("VT_SHARED_SV.DatSet.strVal := 'XXXXXXXXXX'; // tag unavailable")                                            # need to review
    list1.append("VT_SHARED_SV.DatSet.q := VT_SHARED_SV.St_.q; // tag unavailable")                                           # need to review
    list1.append("VT_SHARED_SV.SvID.strVal := 'XXXXXXXXXX'; // tag unavailable")                                              # need to review
    list1.append("VT_SHARED_SV.SvID.q := VT_SHARED_SV.St_.q; // tag unavailable")                                             # need to review
    list1.append("VT_SHARED_SV.Addr.strVal := 'XXXXXXXXXX'; // tag unavailable")                                              # need to review
    list1.append("VT_SHARED_SV.Addr.q := VT_SHARED_SV.St_.q; // tag unavailable")                                             # need to review
    list1.append("VT_SHARED_SV.VlanID.strVal := 'XXXXXXXXXX'; // tag unavailable")                                            # need to review
    list1.append("VT_SHARED_SV.VlanID.q := VT_SHARED_SV.St_.q; // tag unavailable")                                           # need to review
    list1.append("VT_SHARED_SV.VlanPri.strVal := 'XXXXXXXXXX'; // tag unavailable")                                           # need to review
    list1.append("VT_SHARED_SV.VlanPri.q := VT_SHARED_SV.St_.q; // tag unavailable")                                          # need to review
    list1.append("VT_SHARED_SV.AppID.strVal := 'XXXXXXXXXX'; // tag unavailable")                                             # need to review
    list1.append("VT_SHARED_SV.AppID.q := VT_SHARED_SV.St_.q; // tag unavailable")                                            # need to review
    return(list1)

def pgpopulateptp(arg1):
    list1 = []
    name1 = str(arg1)
    list1.append("VT_SHARED_PTP.LTIM_TmDt := " + str(name1) + "_850.CFG.LTIM1.TmDT;")
    list1.append("VT_SHARED_PTP.LTMS_TmAcc.strVal := DINT_TO_STRING(" + str(name1) + "_850.CFG.LTMS1.TmAcc.stVal);")
    list1.append("VT_SHARED_PTP.LTMS_TmAcc.q := " + str(name1) + "_850.CFG.LTMS1.TmAcc.q;")
    list1.append("VT_SHARED_PTP.LTMS_TmSrcTyp := TmSrcTyp_PTP(" + str(name1) + "_850.CFG.LTMS1.SelTmSrcTyp);")
    list1.append("VT_SHARED_PTP.LTMS_TmSyn := TmSyn_PTP(" + str(name1) +"_850.CFG.LTMS1.SelTmSyn);")
    list1.append("VT_SHARED_PTP.LTMS_TmTosPer.strVal := REAL_TO_STRING(" + str(name1) + "_850.CFG.LTMS1.SelTmTosPer.instMag);")
    list1.append("VT_SHARED_PTP.LTMS_TmTosPer.q := " + str(name1) + "_850.CFG.LTMS1.SelTmTosPer.q;")
    list1.append("IF " + str(name1) + "_850.CFG.LTMS1.SelTmSynLkd.stVal = 1 THEN")
    list1.append("\tVT_SHARED_PTP.LTMS_St.stVal := TRUE;")
    list1.append("ELSE")
    list1.append("\tVT_SHARED_PTP.LTMS_St.stVal := FALSE;")
    list1.append("END_IF")
    list1.append("VT_SHARED_PTP.LTMS_St.q := " + str(name1) + "_850.CFG.LTMS1.SelTmSynLkd.q;")
    list1.append("VT_SHARED_PTP.LTMS_St.t := " + str(name1) + "_850.CFG.LTMS1.SelTmSynLkd.t;")                 
    list1.append("VT_SHARED_PTP.ID.strVal := '" + str(name1) + "'; // tag unavailable")                                     # need to review
    list1.append("VT_SHARED_PTP.ID.q := VT_SHARED_PTP.LTMS_St.q; // tag unavailable")                                       # need to review
    list1.append("VT_SHARED_PTP.LTIM_TmUseDT.stVal := FALSE; // tag unavailable")                                           # need to review
    list1.append("VT_SHARED_PTP.LTIM_TmUseDT.q := VT_SHARED_PTP.LTMS_St.q; // tag unavailable")                             # need to review
    list1.append("VT_SHARED_PTP.LTIM_TmOfsTmm.strVal := 'XXXXXXXXXX'; // tag unavailable")                                  # need to review
    list1.append("VT_SHARED_PTP.LTIM_TmOfsTmm.q := VT_SHARED_PTP.LTMS_St.q; // tag unavailable")                            # need to review
    list1.append("VT_SHARED_PTP.LTIM_TmChgDT.strVal := 'XXXXXXXXXX'; // tag unavailable")                                   # need to review
    list1.append("VT_SHARED_PTP.LTIM_TmChgDT.q := VT_SHARED_PTP.LTMS_St.q; // tag unavailable")                             # need to review
    list1.append("VT_SHARED_PTP.LTIM_TmChgST.strVal := 'XXXXXXXXXX'; // tag unavailable")                                   # need to review
    list1.append("VT_SHARED_PTP.LTIM_TmChgST.q := VT_SHARED_PTP.LTMS_St.q; // tag unavailable")                             # need to review
    list1.append("VT_SHARED_PTP.LTMS_TmSrc.strVal := 'XXXXXXXXXX'; // tag unavailable")                                     # need to review
    list1.append("VT_SHARED_PTP.LTMS_TmSrc.q := VT_SHARED_PTP.LTMS_St.q; // tag unavailable")                               # need to review
    return(list1)

def pgselectgoose():
    file = open(r"PG_SELECT_GOOSE.txt", "w+")
    flag1 = 1
    for obj1 in list_device:
        for i in range(1, int(obj1.lgos) + 1):
            if flag1 == 1:
                str1 = "IF VT_SELECT_GOOSE." + str(obj1.name) + "_LGOS" + str(i) + "_Select.operPulse.ctlVal THEN" + "\n"
                file.write(str1)
                flag1 = 0
            else:
                str2 = "ELSIF VT_SELECT_GOOSE." + str(obj1.name) + "_LGOS" + str(i) + "_Select.operPulse.ctlVal THEN" + "\n"
                file.write(str2)
            for obj2 in list_device:
                for j in range(1, int(obj2.lgos) + 1):
                    str3 = str(obj2.name) + "_LGOS" + str(i)
                    str4 = str(obj1.name) + "_LGOS" + str(j)
                    if str3 == str4:
                        str5 = "\tVT_SELECT_GOOSE." + str(obj2.name) + "_LGOS" + str(j) + ".stVal := TRUE;" + "\n"
                        file.write(str5)
                    else:
                        str6 = "\tVT_SELECT_GOOSE." + str(obj2.name) + "_LGOS" + str(j) + ".stVal := FALSE;" + "\n"
                        file.write(str6)   
    file.write("END_IF")
    file.close

def pgselectsv():
    file = open(r"PG_SELECT_SV.txt", "w+")
    flag2 = 1
    for obj1 in list_device:
        if obj1.svmd == "sub":
            for i in range(1, int(obj1.lsvs) + 1):
                if flag2 == 1:
                    str1 = "IF VT_SELECT_SV." + str(obj1.name) + "_LSVS" + str(i) + "_Select.operPulse.ctlVal THEN" + "\n"
                    file.write(str1)
                    flag2 = 0
                else:
                    str2 = "ELSIF VT_SELECT_SV." + str(obj1.name) + "_LSVS" + str(i) + "_Select.operPulse.ctlVal THEN" + "\n"
                    file.write(str2)
                for obj2 in list_device:
                    if obj2.svmd == "sub":
                        for j in range(1, int(obj2.lsvs) + 1):
                            str3 = str(obj2.name) + "_LSVS" + str(i)
                            str4 = str(obj1.name) + "_LSVS" + str(j)
                            if str3 == str4:
                                str5 = "\tVT_SELECT_SV." + str(obj2.name) + "_LSVS" + str(j) + ".stVal := TRUE;" + "\n"
                                file.write(str5)
                            else:
                                str6 = "\tVT_SELECT_SV." + str(obj2.name) + "_LSVS" + str(j) + ".stVal := FALSE;" + "\n"
                                file.write(str6)                   
    file.write("END_IF")
    file.close

def pgpopulatesv_main():
    file = open(r"PG_POPULATE_SV.txt", "w+")
    flag1 = 1
    for obj1 in list_device:
        if obj1.svmd == "sub":
            for i in range(1, int(obj1.lsvs) + 1):
                if flag1 == 1:
                    str1 = "IF VT_SELECT_SV." + str(obj1.name) + "_LSVS" + str(i) + ".stVal THEN" + "\n"
                    file.write(str1)
                    x = pgpopulatesv(obj1.name,i)
                    for j in range(0, len(x)):
                        str2 = "\t" + x[j] + "\n"
                        file.write(str2);
                    flag1 = 0
                else:
                    str1 = "ELSIF VT_SELECT_SV." + str(obj1.name) + "_LSVS" + str(i) + ".stVal THEN" + "\n"
                    file.write(str1)
                    x = pgpopulatesv(obj1.name,i)
                    for j in range(0, len(x)):
                        str2 = "\t" + x[j] + "\n"
                        file.write(str2);
    file.write("END_IF")
    file.close

def pgselectptp():
    file = open(r"PG_SELECT_PTP.txt", "w+")
    flag3 = 1
    for obj1 in list_device:
        if flag3 == 1:
            str1 = "IF VT_SELECT_PTP." + str(obj1.name) + "_Select.operPulse.ctlVal THEN" + "\n"
            file.write(str1)
            flag3 = 0
        else:
            str2 = "ELSIF VT_SELECT_PTP." + str(obj1.name) + "_Select.operPulse.ctlVal THEN" + "\n"
            file.write(str2)

        for obj2 in list_device:
            str3 = str(obj2.name)
            str4 = str(obj1.name)
            if str3 == str4:
                str5 = "\tVT_SELECT_PTP." + str(obj2.name) + ".stVal := TRUE;" + "\n"
                file.write(str5)
            else:
                str6 = "\tVT_SELECT_PTP." + str(obj2.name) + ".stVal := FALSE;" + "\n"
                file.write(str6)       
    file.write("END_IF")
    file.close

def pgpopulateptp_main():
    file = open(r"PG_POPULATE_PTP.txt", "w+")
    for obj1 in list_device:
        str1 = "VT_INDIVIDUAL_PTP." + str(obj1.name) + " := TmSynLkd_PTP(SEL_400G_1_850.CFG.LTMS1.SelTmSynLkd);\n"
        file.write(str1)
    flag4 = 1
    for obj2 in list_device:
        if flag4 == 1:
            str2 = "IF VT_SELECT_PTP." + str(obj2.name) + ".stVal THEN" + "\n"
            file.write(str2)
            x = pgpopulateptp(obj2.name)
            for j in range(0, len(x)):
                str3 = "\t" + x[j] + "\n"
                file.write(str3);
            flag4 = 0      
        else:
            str2 = "ELSIF VT_SELECT_PTP." + str(obj2.name) + ".stVal THEN" + "\n"
            file.write(str2)
            x = pgpopulateptp(obj2.name)
            for j in range(0, len(x)):
                str3 = "\t" + x[j] + "\n"
                file.write(str3);
    file.write("END_IF")
    file.close

def pgpopulateprp_main():
    file = open(r"PG_POPULATE_PRP.txt", "w+")       
    flag5 = 1
    for obj2 in list_device:
        if flag5 == 1:
            str2 = "IF VT_SELECT_PRP." + str(obj2.name) + ".stVal THEN" + "\n"
            file.write(str2)
            x = pgpopulateprp(obj2.name)
            for j in range(0, len(x)):
                str3 = "\t" + x[j] + "\n"
                file.write(str3);
            flag5 = 0  
        else:
            str2 = "ELSIF VT_SELECT_PRP." + str(obj2.name) + ".stVal THEN" + "\n"
            file.write(str2)
            x = pgpopulateprp(obj2.name)
            for j in range(0, len(x)):
                str3 = "\t" + x[j] + "\n"
                file.write(str3);
    file.write("END_IF")
    file.close

def pgpopulateprp(arg1):
    name1 = str(arg1)
    str01 = "VT_SHARED_PRP.ID.strVal := '" + str(name1) + ".PRPGGIO1';"
    if name1 == 'SEL_400G_1':
        str02 = "VT_SHARED_PRP.PRPAGOK := " + str(name1) + "_850.ANN.PRPGGIO47.Ind01;"
        str03 = "VT_SHARED_PRP.PRPBGOK := " + str(name1) + "_850.ANN.PRPGGIO47.Ind02;"
        str04 = "VT_SHARED_PRP.PRPCGOK := " + str(name1) + "_850.ANN.PRPGGIO47.Ind03;"
        str05 = "VT_SHARED_PRP.PRPDGOK := " + str(name1) + "_850.ANN.PRPGGIO47.Ind04;"
        str06 = "VT_SHARED_PRP.PRPASOK := " + str(name1) + "_850.ANN.PRPGGIO47.Ind05;"
        str07 = "VT_SHARED_PRP.PRPBSOK := " + str(name1) + "_850.ANN.PRPGGIO47.Ind06;"
    else:
        str02 = "VT_SHARED_PRP.PRPAGOK := " + str(name1) + "_850.ANN.PRPGGIO1.Ind01;"
        str03 = "VT_SHARED_PRP.PRPBGOK := " + str(name1) + "_850.ANN.PRPGGIO1.Ind02;"
        str04 = "VT_SHARED_PRP.PRPCGOK := " + str(name1) + "_850.ANN.PRPGGIO1.Ind03;"
        str05 = "VT_SHARED_PRP.PRPDGOK := " + str(name1) + "_850.ANN.PRPGGIO1.Ind04;"
        str06 = "VT_SHARED_PRP.PRPASOK := " + str(name1) + "_850.ANN.PRPGGIO1.Ind05;"
        str07 = "VT_SHARED_PRP.PRPBSOK := " + str(name1) + "_850.ANN.PRPGGIO1.Ind06;"
    list_device1 = [str01, str02, str03, str04, str05, str06, str07]
    return(list_device1)

def pgselectprp():
    file = open(r"PG_SELECT_PRP.txt", "w+")
    flag3 = 1
    for obj1 in list_device:
        if flag3 == 1:
            str1 = "IF VT_SELECT_PRP." + str(obj1.name) + "_Select.operPulse.ctlVal THEN" + "\n"
            file.write(str1)
            flag3 = 0
        else:
            str2 = "ELSIF VT_SELECT_PRP." + str(obj1.name) + "_Select.operPulse.ctlVal THEN" + "\n"
            file.write(str2)
        for obj2 in list_device:
            str3 = str(obj2.name)
            str4 = str(obj1.name)
            if str3 == str4:
                str5 = "\tVT_SELECT_PRP." + str(obj2.name) + ".stVal := TRUE;" + "\n"
                file.write(str5)
            else:
                str6 = "\tVT_SELECT_PRP." + str(obj2.name) + ".stVal := FALSE;" + "\n"
                file.write(str6)                 
    file.write("END_IF")
    file.close

#pgselectgoose()
#pgselectprp()
#pgselectptp()
#pgselectsv()
#pgpopulategoose_main()
#pgpopulateprp_main()
#pgpopulateptp_main() 
#pgpopulatesv_main()
#wtvtsharedgoose()
#wtvtsharedsv()
#wtvtsharedptp()

print("End")
