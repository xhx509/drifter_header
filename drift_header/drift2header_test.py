# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 10:26:26 2015

@author: hxu
"""

# -*- coding: utf-8 -*-
"""
Created on Wed May  9 09:26:09 2012
routine to write header lines for "drift_header" table in oracle
@author: jmanning
"""
from matplotlib import mlab as ml
import sys
sys.path.append('/net/home3/ocn/jmanning/py/mygit/modules/')
from getdata import get_w_depth
from conversions import dd2dm
from matplotlib.dates import num2date
import numpy as np

############ 
##HARDCODES
mthyr='feb2015' # mthyr of processing
############
f=open('/net/data5/jmanning/drift/drift2header_'+mthyr+'.out','w'); # opens output file        
#pipe = subprocess.Popen(["perl", "/home3/ocn/jmanning/sql/getdrift_header.plx"
# this reads a list of ids that need to be loaded into drift_header table from a file like drift2header_'+mthyr+'mar2013.dat
# which is created by running the code "update_drift_header.py"
# It gets LAT_START,LON_START,BTM_DEPTH_START,START_DATE,DROGUE_DEPTH_START,
# DROGUE_DEPTH_END where start and end drogue depth is in the
# vertical dimension and the _data file list only the midvalue
#d=ml.load('/net/data5/jmanning/drift/sqldump_header.dat')
d=ml.load('/net/data5/jmanning/drift/sqldump_header.dat') # loads list of 
codes=ml.load('/net/data5/jmanning/drift/codes.dat')
jj=0
for k in range(len(d)):
  if len(set([d[k,0]]).intersection(set([138410703,146410701]))):
    if (d[k,0]==138410703):
       deployer='SEA    ' # 12 character deployer name
       notes='deployed by undergrad students, the aluminum surface drifter went silent on 10 September, recovered by Chathams Harbormaster Stuart Smith, and picked up by Miles Manning; the 12m drogue (25 Aug) dragged bottom on Tuckernuck Shoals until Dick Limeburner recovered it in mid-October'
       typei='Irina  '
       droguetop=0
       droguebot=1.0
       droguedia=1.0      
    elif d[k,0]==146410701:
       deployer='Tiejie'
       notes='deployed by Hollings students, Conner and Ed; apparently lost drogue 3 weeks later, came ashore on Craigville Beach, possibly taken home by someone to Yarmouth'
       typei='Drogue  '
       typei='Irina  '
       droguetop=0
       droguebot=1.0
       droguedia=1.0
    pi='Manning'
    institute='NEFSC   '
    project='Drifter_test  '
    manufacturer='NEFSC        '
    communication='GLOBALSTAR'
    accuracy=300
  elif ((d[k,0]==130410702) or (d[k,0]==130410706) or (d[k,0]==130410703) or (d[k,0]==130410704) or (d[k,0]==130410705) or (d[k,0]==130410708)):
    deployer='McManus    ' # 12 character deployer name
    pi='Bell'
    institute='Audubon   '
    project='Nauset High  '
    if d[k,0]==130410702:
        typei='turtle  '
        droguetop=0
        droguebot=0.2
        droguedia=0.4
    else:
        typei='Irina  '
        droguetop=0
        droguebot=1.0
        droguedia=1.0
    manufacturer='Audubon        '
    communication='GLOBALSTAR'
    accuracy=300
    notes=''
  elif ((d[k,0]>=117380761) and (d[k,0]<=117380763)):
    deployer='Salisbury    ' # 12 character deployer name
    pi='Salisbury'
    institute='UNH   '
    project='Acidification  '
    typei='Eddie  '
    manufacturer='SMCC        '
    communication='GLOBALSTAR'
    accuracy=300
    droguetop=0
    droguebot=1
    droguedia=1
  elif (d[k,0]==146410701) or (d[k,0]==146430702) or (d[k,0]==146430703):
    deployer='Tioga        ' # 12 character deployer name
    pi='Kirincich'
    institute='WHOI   '
    project='Education  '
    typei='Irina  '
    manufacturer='WHOI        '
    communication='GLOBALSTAR'
    accuracy=300
    droguetop=0
    droguebot=1
    droguedia=1
    notes='Kama Thieler prepared'
  elif (d[k,0]==140350771) or (d[k,0]==140350772):
    deployer='Deagan        ' # 12 character deployer name
    pi='Deagan'
    institute='CFCC   '
    project='CFCC  '
    typei='Eddie  '
    manufacturer='CFCC        '
    communication='GLOBALSTAR'
    accuracy=300
    droguetop=0
    droguebot=1
    droguedia=1
    notes='both on their way with the Gulf Stream apparently went down in a hurricane'
  elif len(set([d[k,0]]).intersection(set([149410720,149410721,149410725])))>0:
    deployer='Tobias      ' # 12 character deployer name
    pi='Tobias'
    institute='UCONN   '
    project='Chemistry  '
    typei='Sean  '
    manufacturer='UCONN         '
    communication='GLOBALSTAR'
    accuracy=300
    droguetop=0
    droguebot=1
    droguedia=1
    notes='had other instruments aboard'
  elif (d[k,0]==145420701) or (d[k,0]==145420702):
    deployer='Wilbur      ' # 12 character deployer name
    pi='Wilbur '
    institute='SHS   '
    project='SHS   '
    typei='Eddie  '
    manufacturer='SHS         '
    communication='GLOBALSTAR'
    accuracy=300
    droguetop=0
    droguebot=1
    droguedia=1
    notes='floats and PVC spars; blown into harbor given a few days of easterlies so one landed in the Saugus mud flats and one landed on Georges Island but later recovered by Donald from Boston Harbor Auth'
  elif len(set([d[k,0]]).intersection(set([130590046,130590047,130590033,130590034,130590041,130590042,130590043,130590044,130590045])))>0:
    deployer='Hughes      ' # 12 character deployer name
    pi='Hughes '
    institute='Scotland'
    project='HF Radar   '
    typei='Sean  '
    manufacturer='Scotland'
    communication='GLOBALSTAR'
    accuracy=300
    droguetop=0
    droguebot=1
    droguedia=1
    notes=''
  elif (d[k,0]==139420691):
    deployer='Klimkosky      ' # 12 character deployer name
    pi='Klimkosky '
    institute='TruroCentral'
    project='   '
    typei='Eddie  '
    if d[k,0]==139420692:
        typei='Cassie'
    manufacturer='JiM         '
    communication='GLOBALSTAR'
    accuracy=300
    droguetop=0
    droguebot=1
    droguedia=1
    notes='deployed by fishermen from Truro, MA; TCS unit quit on 23 Nov while BFS unit got into the Gulf Stream and died our near the Grand Banks in late January 2014'
  elif (d[k,0]==134410711) or (d[k,0]==139400721):
    deployer='Bomster     ' # 12 character deployer name
    pi='Horrigan'
    institute='NESS  '
    project='NESS  '
    if d[k,0]==139400721:
      typei='Cassie  '
    manufacturer='NESS        '
    communication='GLOBALSTAR'
    accuracy=300
    droguetop=0
    droguebot=1
    droguedia=1  
  elif (d[k,0]>=140420801) and (d[k,0]<=140420803):
    deployer='Boughton    ' # 12 character deployer name
    pi='Boughton'
    institute='PSU   '
    project='PSU  '
    typei='Eddie  '
    manufacturer='PSU        '
    communication='GLOBALSTAR'
    accuracy=300
    droguetop=0
    droguebot=1
    droguedia=1
    notes='deployed by border patrol, headed intially west, one reporting less than the other, and all came ashore'
  elif len(set([d[k,0]]).intersection(set([146450841,146450842,146450843,146450831,146450832,148460851,148460852,148460853]))):
    deployer='Fahnenstiel    ' # 12 character deployer name
    pi='McCormick'
    institute='GLERL   '
    project='GLERL  '
    typei='Eddie  '
    manufacturer='GLERL        '
    communication='GLOBALSTAR'
    accuracy=300
    droguetop=0
    droguebot=1
    droguedia=1
    if d[k,0]>148460850:
      notes='two came ashore in early September (one on north shore of Lake Michigan and one on Bois Blanc Island) and the other quit 26 Sept in mid-Lake Huron '
    elif d[k,0]<146450833:
       notes='hugged the coast and apparently came ashore just east of Hammond Bay on 9 June' 
    else:
       notes='quickly moved into Huron; reversed direction; one landed on Bois Blanc Island on 26 June; one at St Ignace; one went back into Lake Michigan and landed quite away up along the northern shore on a Brevoort beach on 2 July '
  elif len(set([d[k,0]]).intersection(set([138430702,138430704,138430706,139430701])))>0:
    deployer='Goldstein    ' # 12 character deployer name
    pi='Goldstein'
    institute='NEFSC   '
    project='Lobster  '
    typei='Bucket  '
    manufacturer='UNH        '
    communication='GLOBALSTAR'
    accuracy=300
    droguetop=0
    droguebot=.5
    droguedia=.3
  elif (d[k,0]==131430701) or (d[k,0]==130430701):
    deployer='Tarbox    ' # 12 character deployer name
    pi='Long'
    institute='SMCC   '
    project='SMCC  '
    typei='Eddie  '
    manufacturer='SMCC        '
    communication='GLOBALSTAR'
    accuracy=300
    droguetop=0
    droguebot=1
    droguedia=1
    notes=''
  #elif len(set([d[k,0]]).intersection(set([120290881,120290882,1202900883,120290884,120920371,120920372,120920373,120920374,133120371,133120372,133120373,133120374,135120371,135120372,135120373,135280891,135280892,135280893,135280894])))>0:
  elif len(set([d[k,0]]).intersection(set([145280891,145280892,145280893,145280894,145280894,145280895,145280896,146290891,146290892,146290893,146290894,147340751])))>0:
    deployer='Mansfield  '
    pi='Mansfield'
    institute='UCF'
    project='Turtles    '
    if  (d[k,0]==146290891) or (d[k,0]==146290894):
      typei='Bucket'
      droguebot=0.5
      droguedia=0.6     
    elif  (d[k,0]==145280891) or (d[k,0]==145280893) or (d[k,0]==145280896):
      typei='Bucket'
      droguebot=0.5
      droguedia=0.6     
    else:
      typei='Eddie   '
      droguebot=1.0
      droguedia=1.0  
    manufacturer='SMCC'
    communication='GLOBALSTAR'
    accuracy=300
    droguetop=0
    notes='deployed alongside turtles; 3 washed ashore weeks later in the shallowsof Terrebonne Bay; two went west and both ashore by the end of June; and one died on 27 June'
  elif len(set([d[k,0]]).intersection(set([137440661,145430691,14360701])))>0:
    deployer='Tioga    ' # 12 character deployer name
    pi='Terry'
    institute='GOMI '
    project='Education  '
    typei='Eddie   '
    manufacturer='GOMI         '
    communication='GLOBALSTAR'
    accuracy=300
    droguetop=0
    droguebot=1.0
    droguedia=1.0
    notes=''
  elif len(set([d[k,0]]).intersection(set([148460851])))>0:
    deployer='McCormick    ' # 12 character deployer name
    pi='Ruberg'
    institute='GLERL '
    project='Education  '
    typei='Eddie   '
    manufacturer='GLERL         '
    communication='GLOBALSTAR'
    accuracy=300
    droguetop=0
    droguebot=1.0
    droguedia=1.0
    notes='quit 26 Sept in mid-Lake Huron '
  elif len(set([d[k,0]]).intersection(set([137410702,130410701,148410712])))>0:
    deployer='SeaKeepers    ' # 12 character deployer name
    pi='McFadden'
    institute='MCC '
    project='Education  '
    typei='Irina'
    manufacturer='NEFSC         '
    communication='GLOBALSTAR'
    accuracy=300
    droguetop=0
    droguebot=1.0
    droguedia=1.0
    notes='suddenly went silent in the channel between Montauk and Block Island three days after deployment'
  elif (len(set([d[k,0]]).intersection(set(range(145600041,145600049))))>0) or (len(set([d[k,0]]).intersection(set([130590048])))>0):
    deployer='Hughes   ' # 12 character deployer name
    pi='Hughes'
    institute='Scotland '
    project='HFR_validate'
    typei='Sean   '
    manufacturer='Scotland        '
    communication='GLOBALSTAR'
    accuracy=300
    droguetop=0
    droguebot=1.0
    droguedia=1.0
    notes='Fitted with plastic boxes and deployed alongside standard drogued drifters; some lasted weeks and some lasted months; one landed on SE coast of Shetland Island'
  elif len(set([d[k,0]]).intersection(set(range(147420701,147420708))))>0:
    deployer='Whitney    ' # 12 character deployer name
    pi='Whitney'
    institute='UCONN '
    project='Charles Morgan  '
    typei='Sean   '
    manufacturer='UCONN         '
    communication='GLOBALSTAR'
    accuracy=300
    droguetop=0
    droguebot=1.0
    droguedia=1.0
    notes='a few went into the deep gulf, a few went south to Great South Channel and on to Georges Bank. All survived at least a week and as long as 3+ months.'
  elif len(set([d[k,0]]).intersection(set(range(148410720,148410729))))>0:
    deployer='Whitney    ' # 12 character deployer name
    pi='Whitney'
    institute='UCONN '
    project='River Plume  '
    typei='Cassie   '
    manufacturer='UCONN         '
    communication='GLOBALSTAR'
    accuracy=300
    droguetop=0
    droguebot=1.0
    droguedia=1.0
    notes='the first few were short tracks inside a small bay, a few landed on Fishers Island, a few recovered by fishermen, and a few went on to the shelf '
  elif len(set([d[k,0]]).intersection(set(range(140240801,140240808))))>0:
    deployer='Dierssen    ' # 12 character deployer name
    pi='Dierssen'
    institute='UCONN '
    project='Seaweed  '
    typei='Bucket   '
    manufacturer='SMCC         '
    communication='GLOBALSTAR'
    accuracy=300
    droguetop=0
    droguebot=0.5
    droguedia=0.3
  elif len(set([d[k,0]]).intersection(set([140410701,140410702,140410703,140410706])))>0:
    deployer='Prescott    ' # 12 character deployer name
    pi='Prescott'
    institute='Audubon'
    project='turtles  '
    typei='Bucket   '
    manufacturer='Audubon'
    communication='GLOBALSTAR'
    accuracy=300
    droguetop=0
    droguebot=0.5
    droguedia=0.3
    if d[k,0]==140410701:
      notes='drifter groundings 1-2 days later at Barnstable Harbor after strong north winds'
    elif d[k,0]==140410706:
      notes='drifter grounding 2 weeks later on the other side of Cape Cod Bay (north of Sagamore Beach) 5 weeks later another on Jeremey Point and picked up'
    elif d[k,0]==140410703:
      notes='drifter groundings 1-2 days later on Jeremy Point'
    elif d[k,0]==140410702:
      notes='5 weeks later another on Jeremey Point and picked up'
  elif len(set([d[k,0]]).intersection(set([148420701,148420702,148420703,148420707,148420708,148420709,1484207010])))>0:
    deployer='Doherty   ' # 12 character deployer name
    pi='Buckley'
    institute='CSCR '
    project='Education  '
    typei='Irina   '
    manufacturer='CSCR         '
    communication='GLOBALSTAR'
    accuracy=300
    droguetop=0
    droguebot=1.0
    droguedia=1.0
    if d[k,0]==148420703:
      notes='died 3 months later on NE Peak of Georges Bank'
    elif d[k,0]==148420701:
      notes='died 3 months later on south side of Georges Bank'
    elif d[k,0]==148420708:
      notes='landed on Truro backside beach recovered by Joe, the beachwalker'
    elif d[k,0]==148420707:
      notes='Flowed into Barnstable Harbor recovered by Greg Hamm'
    elif d[k,0]==148420709:
      notes='laned 2 days later on Scituate Beach recovered by Fran Smith'
    elif d[k,0]==148420702:
      notes='landed 2 weeks later near Manchester by the Sea recovered by Deidre'
  elif len(set([d[k,0]]).intersection(set([148190741,148190742,148250813,148250814])))>0:
    deployer='Garson      ' # 12 character deployer name
    pi='Garson'
    institute='OET'
    project='Education'
    manufacturer='OET          '
    communication='GLOBALSTAR'
    accuracy=300
    notes='drogued recovered by Belize fishermen and expect to be redeployed; while the other surface drifter went on to a reef, was apparently recovered on 24 Aug and brought into the port of Corozal'
    if (d[k,0]==148190741):
       typei='Drogue   '
       droguetop=15.
       droguebot=19.
       droguedia=0.3
       notes='drogued recovered by Belize fishermen'
    else:
        typei='Irina  '
        droguetop=0
        droguebot=1.0
        droguedia=1.0    
        notes='went on to a reef, was apparently recovered on 24 Aug and brought into the port of Corozal'
  elif len(set([d[k,0]]).intersection(set([145310811,145310812,149310811,149310812])))>0:
    deployer='Peterson   ' # 12 character deployer name
    pi='Peterson'
    institute='GRNMS'
    project='Education'
    manufacturer='GRNMS     '
    communication='GLOBALSTAR'
    accuracy=300
    if d[k,0]<149310811:
      notes='set with dye in big runoff event; oscillated with tide; caught in Gulf Stream and apparetnly went down with Hurrican Arthur on July 3rd.'
    else:
      notes='student built at workshop; swashed with the river-mouth tide the first few days and came ashore a few miles up river.'
    droguetop=0
    droguebot=1.0
    droguedia=1.0    
  elif len(set([d[k,0]]).intersection(set([140410709,1404107011])))>0:
    deployer='Galuzzo    ' # 12 character deployer name
    pi='Galuzzo '
    institute='SSNSC'
    project='Education'
    manufacturer='SSNSC     '
    communication='GLOBALSTAR'
    accuracy=300
    notes=''
    droguetop=0
    droguebot=1.0
    if d[k,0]==1404107011:
      notes='landed on Truro Beach on 2 Jan, called in by Jack Adams, the realtor, recovered by Bob Prescott.'
    else:
      notes='died a few days in'
  elif len(set([d[k,0]]).intersection(set([140410707,140410708])))>0:
    deployer='Jesse       '#
    pi='Gawarkewicz'
    institute='WHOI'
    project='Education'
    manufacturer='Falm_Academy'
    communication='GLOBALSTAR'
    accuracy=300
    droguetop=0
    droguebot=1.0
    droguedia=1.0    
    droguedia=1.0    
    if d[k,0]==140410707:
       notes='Landed near Pilgrim Power Plant intake!'
       typei='Irina'
    else:
       notes='floatie flotation and fiberglass spars died 2 weeks later in storm'
       typei='Megan'
  elif len(set([d[k,0]]).intersection(set(range(147430861,147430865))))>0:
    deployer='Xia      '#
    pi='Xia'
    institute='UMaryland'
    project='Education'
    manufacturer='NEFSC'
    communication='GLOBALSTAR'
    accuracy=300
    notes='one ashore a week later while the others went as far as the northern shore and islands of the lake in late September '
    droguetop=0
    droguebot=1.0
    droguedia=1.0    
    droguedia=1.0    
  else:
    deployer=0  

  # find serieal number in codes.dat file  
  if deployer<>0:
      jj=jj+1; # keep track of units added
      idsn=ml.find(np.array(map(int,codes[:,1]))==int(d[k,0]))
      if len(idsn)<>0:
          sn=float(map(int,codes[idsn,0])[0])
          #if codes[idsn,2]==0.5:
          #    type='Paul    '
      else:
          print 'no SN for '+str(d[k,0])
      if len(d)<>0:
        wd=get_w_depth([d[k,3]],[d[k,4]])
        #wd=-100
        if wd<-99:
          wd=999 # bad water depth estimate
        [latddmm,londdmm]=dd2dm(d[k,4],d[k,3])
        datet=num2date(d[k,2]).replace(year=int(d[k,1])).strftime('%d-%b-%Y:%H%M') # makes a datetime using year and yearday combination      
        #print 'Processed drifter '+str(d[k,0])+' as deployed by '+deployer+'.'
        #               1     2     3     4     5    6   7      8    9   10 11 12 13 14 15 16
        f.write("%9.0f"%d[k,0]+" %7.2f"%d[k,2]+" %7.2f" %latddmm+" %7.2f"%londdmm+"%5.0f"%wd+' {:<20}'.format(datet)+"%7.1f"%droguetop+"%7.1f"%droguebot+"%7.1f"%droguedia+' {:<20}'.format(project)+'{:<20}'.format(institute)+'{:<20}'.format(pi)+'{:<20}'.format(deployer)+'{:<20}'.format(typei)+'{:<20}'.format(manufacturer)+'{:<20}'.format(communication)+" %7.0f"%accuracy+" %7.0f"%sn+" %7.1f "%d[k,6]+'{:<400}'.format(notes)+"\n")
      else:
          print str(d[k,0])+' not in drift_data table. Press return to continue.'
          raw_input()
  else:
      print 'no metadata listed in code for id '+str(d[k,0])
f.close()          
          
      
