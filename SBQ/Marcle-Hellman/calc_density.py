import math

pub_key = [1, 2, 6, 18, 44, 91, 206, 445, 1026, 2893, 6680, 13942, 30535, 78643, 183515, 345031, 1016960, 2423708, 6073902, 13064025, 24521017, 57336947, 122887282, 268793691, 636347288, 1823035084, 4972258664, 12871644364, 21863828258, 53669349636, 110311979821, 211850086220, 469607664750, 1307336652496, 2424071753278, 5958203064468, 17318543506277, 42107591386752, 90825005586998, 222142335268350, 492469291891371, 1363439368975989, 3260059111748183, 9641444086525882, 22475913465939075, 41201622034366444, 112381609414480283, 325419189843291730, 690210479551654023, 1243205954575939486, 3300776832638948211, 9771788006057347166, 17223464922168733447, 44808131554030503623, 88543278843417791772, 180944740491453724842, 380286469459160016220, 954887443632621192963, 2509000254475650644578, 7342175143770433275047, 12715852356641156580963, 35113196901732536498276, 83380326562534745399748, 217081655871009246444889, 440957974943314114328295, 816823174800241440109619, 1852728116822318693706603, 5111781428760860020613176, 9408935979156060017933057, 21449888171268595491987101, 46010863639704238939125957, 95103118948885271709796420, 187257299172865485241951596, 467944276322971460166553616, 1291187147866732769956741944, 3169473324029669793954359332, 8983844237320665192642382701, 18595141595087780464870644589, 42403675018266882441958878029, 103960707838498506960163407279, 187435536421168031674947322448, 506910082194842879503425207152, 1358474420125437527461375981895, 3600164208908254604925746619665, 8828813264809621582682586434730, 25498534783435153951619336415574, 72269934676394551845595403944873, 134417351382035770684508083845169, 328672356889891213477925309597196, 939975467990902327704610760529141, 1705071618338317578903407920740334, 3541313386321973205121672315431114, 9110507772173130526913477067800193, 25890603847813911827113508689527711, 49434295418987165175142932218336014, 132278120412251381941141541067956336, 393373679262862765116163808922891911, 826090627095569163831879596609027107, 2123971254563168743620790479901324357, 5710452456131096191148351894487094934, 9466555521865362450701772140646655616, 25888817917396473735730591271456392149, 71759407929773372999206301237221623554, 143325501673199438571145227938269468648, 323497425870922561406990028807751255094, 794649869360915579098734045138347014674, 2341934491358641311599789488995864114801, 6706697090010692347604447881628279159993, 12862715081947595252463205316443472086442, 26427145062504385561571780118364699174807, 54029205720783838665528633623277556278039, 155811869212078581420443254962432378447332, 404618610621064139516968069712607163007869, 1104804832005106517867423558403830810064912, 2324540893134685037137407374233624082373260, 6938257653300221542245881240741980459144004, 19512117249289653408554123122125408037909847, 34131837495926248987470447377170740959949790, 70390512643912711982639877745980664688475971, 191936449364963502034662159170460733136588927, 428699236373830169466693620153838144443819409, 971996156745342367646382624497527213654733039, 2227026366063249031041870562343669778835843306, 6131545437509573691510508370102652581797689176, 16763402816970482080249162743916739102718195745, 40422407885189498160766364646865717822386550974, 72530123450016548385754166021405376095406818189, 154684077427539333131514838611217171595028774055, 457153068059114324333123514823858014944312555360, 868829682738129307340117115461276459765893627375, 2538323221676789877911455824250362604905114958472, 4974605071692779139245497432730095381679172359438, 9796846721599796062721304617090756828155525863633, 23845891768990094433354096199546944339335010628864, 68459589505161979000990277442096731250881266809358, 145544794324199757658112384710567262351740624325189, 273794432563436323624940868101089046857591330221233, 618554362101847605676315171136224330541751414840228, 1378043272413373128706949600634016335234263951539569, 3174684031817148516446489408918203206336381313071766, 7699317208818054585898421918320732581823102461870100, 19787399966591922660541001971157205019216337635915567, 36887585940519825949541596778212187131199286227573073, 85402550511972838802845431422717239561983913231299243, 203393480431241502036073796677519255142957092207274329, 415898520980665313048451846759399412458606666777132584, 886009095696666060274273389080001724048771847860245876, 1810361865188435841850503403762768956736697227652244716, 4701932019596381745145747132381164055431617460374419489, 9803667094781580956613875872003658407460435164792550961, 27277997934142022218485025685999532157400766387178107519, 52567793606156787214590623393742734119074772403560739077, 115054161864568984774964288530878751007769136456637448074, 267623460925537995414223788006729251294193391484635148452, 683408662019812622616959123400167774008188777198656307355, 1336397403069958816476776752217312131085484490270281782212, 3943743923086649252510938410644648381673402739984535782509, 7601248772276429426732773428039287930815530409392377657075, 20273340517050895639786976421612050945032392692008825436384, 37890595188545415745760348962125053885498794610459846265153, 83410988353010641565522798792843513572019420564110662494323, 241169270788328790569855787210917592047894772982024134562289, 593006009949754003683633011671245238773166004268111344085098, 1065736415777660136805456944091044104638508479356740208647151, 395704489370469770673087638287324831030263647305641583333062, 56647902410582746745510662152766002723859005583002453350552, 729745496138629901067684989989624735370984348998201884811952, 419864194453850606933793513299954701022050267195105945068366, 1018229847616938120219698175538254077038132941140222639903688, 62673123825736562559690712997399050892484309692727515460097, 1036717481424063539904379944630302559240221240245548447737951, 656067339559700853689811114613070355257630327729669178188028, 616218226003413721478719551515167002295940496549319347046347, 964691721383404589639473869024955135613976371799115487982911, 811525481846148334467046149039664721793657030072087146931066, 200503846409133090199558273368028903106651981841500920781956, 1713595294070813026427261862302571140676688302267219557912372, 1368593574706366773903886883533765949643208836523863074073128, 142642841053899278058776599819082204497942959354818325215599, 119862786409999969316416327902155192978336833240831031752587, 619578065833640814206663307589088689182214650208360725773089, 531624722300848440161588411203553509675790851271919025880774, 1096230800239869377493086309621276066539178046744765584411999, 1193018523036430084269785699234898253864907944056377883998798]

d = len(pub_key) / math.log2(pub_key[-1])
print(d)