import sys
import unittest
from parseData import *

class Lab06TestSuite(unittest.TestCase):

    def test_checkPythonVersion(self):

        currentVersion = sys.version_info
        self.assertGreaterEqual(currentVersion, (3, 4))

    def test_isSplitUsed(self):

        with open("parseData.py", "r") as pyFile:
            sourceCode = pyFile.read()

        self.assertFalse(".split(" in sourceCode)

    def test_getInvalidUsers(self):
        expectedValue = RegularExpressionData.invalidUsers
        actualValue = getInvalidUsers()

        self.assertEqual(actualValue, expectedValue)

    def test_getValidUsers(self):
        expectedValue = RegularExpressionData.validUsers
        actualValue = getValidUsers()

        self.assertEqual(actualValue, expectedValue)

    def test_getUsersWithEmails(self):
        expectedValue = RegularExpressionData.usersWithEmails
        actualValue = getUsersWithEmails()

        self.assertEqual(actualValue, expectedValue)

    def test_getUsersWithPhones(self):
        expectedValue = RegularExpressionData.usersWithPhones
        actualValue = getUsersWithPhones()

        self.assertEqual(actualValue, expectedValue)

    def test_getUsersWithStates(self):
        expectedValue = RegularExpressionData.usersWithStates
        actualValue = getUsersWithStates()

        self.assertEqual(actualValue, expectedValue)

    def test_getUsersWithEmailsAndPhones(self):
        expectedValue = RegularExpressionData.usersWithEmailsAndPhones
        actualValue = getUsersWithEmailsAndPhones()

        self.assertEqual(actualValue, expectedValue)

    def test_getUsersWithEmailsAndStates(self):
        expectedValue = RegularExpressionData.usersWithEmailsAndStates
        actualValue = getUsersWithEmailsAndStates()

        self.assertEqual(actualValue, expectedValue)

    def test_getUsersWithPhonesAndStates(self):
        expectedValue = RegularExpressionData.usersWithPhonesAndStates
        actualValue = getUsersWithPhonesAndStates()

        self.assertEqual(actualValue, expectedValue)

class RegularExpressionData:

    validUsers = [('Abraham Evans', 'abraham_evans@purdue.com', '(779) 443-5086', 'Illinois'),
     ('Alexandra Henderson', 'alexandra.henderson@purdue.com', '(334) 235-6110', 'Alabama'),
     ('Buchanan Valerie', 'buchanan_valerie@purdue.com', '(940) 238-8038', 'Texas'),
     ('Carmen Parker', 'carmen_parker@purdue.com', '(260) 167-1480', 'Indiana'),
     ('Casey Russell', 'casey.russell@purdue.com', '(952) 941-8149', 'Minnesota'),
     ('Charlie Lynch', 'clynch690@purdue.com', '(281) 429-3242', 'Texas'),
     ('Chester Craig', 'chester.craig@purdue.com', '(304) 743-7764', 'West Virginia'),
     ('Clark Bass', 'cbass641@purdue.com', '(339) 589-8568', 'Massachusetts'),
     ('Clarke Bradford', 'clarke.bradford@purdue.com', '(413) 523-7114', 'Massachusetts'),
     ('Clifton Nelson', 'clifton_nelson@purdue.com', '(831) 419-9206', 'California'),
     ('Clifton Stone', 'clifton.stone@purdue.com', '(786) 495-1091', 'Florida'),
     ('Darrell Fleming', 'darrell.fleming@purdue.com', '(920) 999-5770', 'Wisconsin'),
     ('Douglas Casey', 'douglas.casey@purdue.com', '(907) 623-8480', 'Alaska'),
     ('Earnest Hudson', 'earnest.hudson@purdue.com', '(203) 645-3310', 'Connecticut'),
     ('Earnest Kennedy', 'earnest_kennedy@purdue.com', '(878) 950-9482', 'Pennsylvania'),
     ('Evans Lowell', 'evans.lowell@purdue.com', '(916) 578-2377', 'California'),
     ('Evelyn Rice', 'evelyn.rice@purdue.com', '(971) 232-8669', 'Oregon'),
     ('Garry Buchanan', 'garry.buchanan@purdue.com', '(816) 631-4934', 'Missouri'),
     ('Gordon Cain', 'gordon_cain@purdue.com', '(539) 214-6624', 'Oklahoma'),
     ('Jacobs Lynette', 'jlynette332@purdue.com', '(320) 299-9905', 'Minnesota'),
     ('Jared Higgins', 'jared.higgins@purdue.com', '(716) 346-4224', 'New York'),
     ('Jenna Moody', 'jenna_moody@purdue.com', '(731) 902-1745', 'Tennessee'),
     ('Jenna Stone', 'jenna_stone@purdue.com', '(760) 503-7644', 'California'),
     ('Joanna King', 'jking368@purdue.com', '(941) 509-1377', 'Florida'),
     ('Joanna Tucker', 'jtucker575@purdue.com', '(443) 434-2323', 'Maryland'),
     ('Joanne Craig', 'joanne.craig@purdue.com', '(410) 764-6369', 'Maryland'),
     ('Kara Singleton', 'kara.singleton@purdue.com', '(623) 317-5357', 'Arizona'),
     ('Kennedy Alexandra', 'kennedy_alexandra@purdue.com', '(309) 721-9576', 'Illinois'),
     ('Larson Kurt', 'larson.kurt@purdue.com', '(636) 376-5858', 'Missouri'),
     ('Long Jeanne', 'long.jeanne@purdue.com', '(612) 227-4366', 'Minnesota'),
     ('Lorena Parker', 'lorena_parker@purdue.com', '(906) 785-6598', 'Michigan'),
     ('Lowell Carter', 'lowell_carter@purdue.com', '(917) 968-9126', 'New York'),
     ('Lowell Dunn', 'ldunn154@purdue.com', '(408) 786-7957', 'California'),
     ('Lynch Toni', 'lynch.toni@purdue.com', '(618) 838-2495', 'Illinois'),
     ('Lynda Aguilar', 'laguilar435@purdue.com', '(570) 176-6936', 'Pennsylvania'),
     ('Mann Kurt', 'mann_kurt@purdue.com', '(938) 862-6282', 'Alabama'),
     ('Marco Day', 'marco.day@purdue.com', '(503) 125-8264', 'Oregon'),
     ('Matt Day', 'mday82@purdue.com', '(602) 618-6073', 'Arizona'),
     ('Matthews Clifton', 'mclifton753@purdue.com', '(330) 501-2857', 'Ohio'),
     ('Max Matthews', 'mmatthews285@purdue.com', '(475) 979-3937', 'Connecticut'),
     ('Melinda Santiago', 'melinda.santiago@purdue.com', '(706) 891-1442', 'Georgia'),
     ('Molly Bass', 'molly.bass@purdue.com', '(405) 359-5058', 'Oklahoma'),
     ('Moody Sandra', 'moody_sandra@purdue.com', '(972) 299-8771', 'Texas'),
     ('Morris Morris', 'morris_morris@purdue.com', '(603) 540-3272', 'New Hampshire'),
     ('Murphy Byrd', 'murphy_byrd@purdue.com', '(502) 183-9557', 'Kentucky'),
     ('Nelson Mills', 'nelson_mills@purdue.com', '(407) 324-8188', 'Florida'),
     ('Omar Yates', 'omar_yates@purdue.com', '(763) 670-7557', 'Minnesota'),
     ('Orville Lowe', 'orville.lowe@purdue.com', '(256) 189-4367', 'Alabama'),
     ('Otis Miller', 'otis.miller@purdue.com', '(903) 823-1778', 'Texas'),
     ('Otis Murphy', 'otis.murphy@purdue.com', '(213) 244-8388', 'California'),
     ('Powers Aguilar', 'powers_aguilar@purdue.com', '(201) 883-7529', 'New Jersey'),
     ('Shannon Sims', 'ssims223@purdue.com', '(530) 447-8319', 'California'),
     ('Stacy Baker', 'stacy_baker@purdue.com', '(385) 930-8641', 'Utah'),
     ('Stone Cecil', 'stone_cecil@purdue.com', '(219) 764-4991', 'Indiana'),
     ('Teresa Valdez', 'teresa_valdez@purdue.com', '(567) 771-5799', 'Ohio'),
     ('Terry Clarke', 'terry.clarke@purdue.com', '(314) 193-7040', 'Missouri'),
     ('Terry May', 'tmay363@purdue.com', '(913) 356-5630', 'Kansas'),
     ('Toni Curtis', 'tcurtis585@purdue.com', '(775) 867-8688', 'Nevada'),
     ('Tucker Murphy', 'tmurphy84@purdue.com', '(856) 966-7736', 'New Jersey'),
     ('Valerie Mills', 'valerie_mills@purdue.com', '(212) 867-3716', 'New York'),
     ('Vicki Clark', 'vicki_clark@purdue.com', '(513) 197-7626', 'Ohio'),
     ('Wade Gordon', 'wade.gordon@purdue.com', '(980) 298-5577', 'North Carolina'),
     ('Wayne Hudson', 'wayne_hudson@purdue.com', '(801) 863-2140', 'Utah'),
     ('Webb Gwendolyn', 'wgwendolyn351@purdue.com', '(231) 785-7123', 'Michigan'),
     ('Winifred Watkins', 'winifred.watkins@purdue.com', '(828) 888-1268', 'North Carolina')]

    invalidUsers = ['Alexander Orville',
     'Alma Ryan',
     'Kristen Aguilar',
     'Kristen Bates',
     'Ryan Powell',
     'Tyrone Watson',
     'Valerie Warren']

    usersWithEmails = [('Alexandra Palmer', 'apalmer522@purdue.com'),
     ('Anthony Sims', 'anthony.sims@purdue.com'),
     ('Baker Sandra', 'bsandra113@purdue.com'),
     ('Cain Owen', 'cain.owen@purdue.com'),
     ('Dale Johnson', 'djohnson546@purdue.com'),
     ('Derrick Barber', 'dbarber615@purdue.com'),
     ('Elbert Banks', 'ebanks111@purdue.com'),
     ('Erika Allen', 'erika_allen@purdue.com'),
     ('Garry Nelson', 'garry.nelson@purdue.com'),
     ('Kara Warner', 'kara.warner@purdue.com'),
     ('Kurt Davidson', 'kurt_davidson@purdue.com'),
     ('Marco Rogers', 'mrogers46@purdue.com'),
     ('Mccormick Teresa', 'mteresa66@purdue.com'),
     ('Nina Patrick', 'nina_patrick@purdue.com'),
     ('Ruby Rice', 'ruby_rice@purdue.com')]

    usersWithPhones = [('Ada Kennedy', '(515) 146-5763'),
     ('Adams Jeffery', '(719) 710-2747'),
     ('Bradford Lowe', '(228) 136-7785'),
     ('Cary Wade', '(580) 696-7342'),
     ('Chester Tucker', '(417) 654-9374'),
     ('Delbert Buchanan', '(404) 798-8699'),
     ('Jeanne Palmer', '(973) 798-9036'),
     ('Jeffery Clark', '(206) 498-1350'),
     ('Jesus Norris', '(251) 666-3312'),
     ('Kathleen Valdez', '(540) 407-9717'),
     ('Kenny May', '(970) 591-3514'),
     ('Lillie Lynch', '(516) 440-5338'),
     ('Lucille Hernandez', '(225) 413-3322'),
     ('Lynda Hopkins', '(414) 739-4409'),
     ('Melinda Henderson', '(470) 679-7161'),
     ('Mercedes Cain', '(563) 830-5015'),
     ('Morris Norman', '(901) 574-3947'),
     ('Owen Green', '(660) 262-4766'),
     ('Palmer Palmer', '(859) 751-4202'),
     ('Phillip Jacobs', '(615) 184-6584'),
     ('Richards Bryant', '(505) 648-5534'),
     ('Sandra Robertson', '(424) 545-5858')]

    usersWithStates = [('Andre Powell', 'Florida'),
     ('Angela Campbell', 'Hawaii'),
     ('Anthony Webb', 'New Jersey'),
     ('Bradford Alexander', 'Georgia'),
     ('Calvin Alexander', 'Virginia'),
     ('Charlie Mccormick', 'Washington'),
     ('Delia Powers', 'North Carolina'),
     ('Elbert Elliott', 'California'),
     ('Ginger Long', 'North Carolina'),
     ('Jamie Spencer', 'Michigan'),
     ('Jenny Greene', 'Michigan'),
     ('Kathy Norman', 'California'),
     ('Kurt Elliott', 'Illinois'),
     ('May Jacobs', 'Pennsylvania'),
     ('Meredith Martin', 'Florida'),
     ('Norris Wayne', 'North Carolina'),
     ('Stacy Wise', 'Washington DC')]

    usersWithEmailsAndPhones = [('Adkins Olive', 'adkins_olive@purdue.com', '(617) 729-3094'),
     ('Bryant Benson', 'bryant.benson@purdue.com', '(520) 626-7698'),
     ('Carmen Daniels', 'carmen_daniels@purdue.com', '(216) 597-3016'),
     ('Carter Russell', 'carter.russell@purdue.com', '(319) 468-8681'),
     ('Courtney Garner', 'courtney.garner@purdue.com', '(956) 231-4376'),
     ('Delia Wade', 'delia_wade@purdue.com', '(830) 735-5952'),
     ('Hattie Banks', 'hattie.banks@purdue.com', '(857) 391-2147'),
     ('Hattie Marshall', 'hmarshall604@purdue.com', '(747) 799-6559'),
     ('James Dunn', 'james_dunn@purdue.com', '(442) 962-9132'),
     ('Jeffery Stokes', 'jstokes162@purdue.com', '(321) 774-8897'),
     ('Jill Miller', 'jmiller12@purdue.com', '(802) 570-4391'),
     ('Lisa Douglas', 'ldouglas844@purdue.com', '(561) 375-2815'),
     ('Lucille Larson', 'lucille_larson@purdue.com', '(762) 131-7666'),
     ('Lynette Richardson', 'lynette_richardson@purdue.com', '(331) 410-3228'),
     ('Max Moore', 'max.moore@purdue.com', '(845) 640-5069'),
     ('Nelson Matthews', 'nelson_matthews@purdue.com', '(865) 655-4020'),
     ('Nelson Nina', 'nelson_nina@purdue.com', '(210) 125-9822'),
     ('Norman Long', 'nlong355@purdue.com', '(947) 721-8710'),
     ('Russell Webb', 'rwebb80@purdue.com', '(773) 906-6685'),
     ('Ryan Kathy', 'ryan_kathy@purdue.com', '(484) 629-2823'),
     ('Sandra Webb', 'sandra_webb@purdue.com', '(458) 450-1177'),
     ('Tami Snyder', 'tsnyder836@purdue.com', '(571) 847-5559'),
     ('Teresa Roy', 'troy73@purdue.com', '(325) 217-6280'),
     ('Terri Beck', 'tbeck269@purdue.com', '(479) 947-3426'),
     ('Thomas Meredith', 'thomas.meredith@purdue.com', '(864) 774-8332'),
     ('Vicki Green', 'vgreen458@purdue.com', '(401) 324-2953'),
     ('Warner Powers', 'wpowers480@purdue.com', '(504) 930-7807')]

    usersWithEmailsAndStates = [('Beck Allen', 'beck.allen@purdue.com', 'California'),
     ('Cameron Davidson', 'cameron.davidson@purdue.com', 'Michigan'),
     ('Cecil Marshall', 'cmarshall749@purdue.com', 'North Carolina'),
     ('Cecil Ryan', 'cecil_ryan@purdue.com', 'Georgia'),
     ('Delbert Harvey', 'delbert_harvey@purdue.com', 'Texas'),
     ('Elena Murphy', 'emurphy454@purdue.com', 'Massachusetts'),
     ('Gordon Warner', 'gwarner206@purdue.com', 'Washington'),
     ('Green Spencer', 'gspencer341@purdue.com', 'Maryland'),
     ('Henderson Brandy', 'hbrandy29@purdue.com', 'Virgin Islands'),
     ('King Kathy', 'king.kathy@purdue.com', 'Ohio'),
     ('Lula Thomas', 'lula_thomas@purdue.com', 'Iowa'),
     ('May Mccormick', 'may_mccormick@purdue.com', 'New Jersey'),
     ('Miller Matthews', 'mmatthews737@purdue.com', 'California'),
     ('Mills Vicki', 'mills_vicki@purdue.com', 'Oklahoma'),
     ('Molly Bates', 'molly_bates@purdue.com', 'Kansas'),
     ('Nina Richardson', 'nina.richardson@purdue.com', 'Virginia'),
     ('Orville Singleton', 'osingleton637@purdue.com', 'California'),
     ('Phillip Mann', 'phillip_mann@purdue.com', 'California'),
     ('Watson Max', 'watson.max@purdue.com', 'California'),
     ('Wayne Delgado', 'wayne.delgado@purdue.com', 'New York')]

    usersWithPhonesAndStates = [('Aguilar Nelson', '(681) 368-8284', 'West Virginia'),
     ('Angela Thomas', '(517) 137-9091', 'Michigan'),
     ('Benson Delgado', '(510) 886-8089', 'California'),
     ('Byrd Watson', '(316) 707-3411', 'Kansas'),
     ('Calvin Moore', '(507) 946-2200', 'Minnesota'),
     ('Cary Evans', '(806) 530-5932', 'Texas'),
     ('Casey Morris', '(814) 618-2538', 'Pennsylvania'),
     ('Elena Goodwin', '(804) 425-9991', 'Virginia'),
     ('Elvira Daniels', '(661) 869-7417', 'California'),
     ('Elvira Hicks', '(336) 267-9410', 'North Carolina'),
     ('Frances Larson', '(765) 895-8700', 'Indiana'),
     ('Gina Adams', '(419) 539-3774', 'Ohio'),
     ('Gwendolyn Houston', '(208) 934-4208', 'Idaho'),
     ('Higgins Derrick', '(936) 678-8220', 'Texas'),
     ('Jeanne Douglas', '(214) 376-2171', 'Texas'),
     ('Joyce Adkins', '(684) 333-4347', 'American Samoa'),
     ('Michael Long', '(702) 927-3351', 'Nevada'),
     ('Olive Bryan', '(715) 312-4742', 'Wisconsin'),
     ('Olson Thomas', '(985) 864-6192', 'Louisiana'),
     ('Owen Santiago', '(318) 782-6643', 'Louisiana'),
     ('Parker Jared', '(805) 991-1829', 'California'),
     ('Pat Byrd', '(929) 561-8197', 'New York'),
     ('Powell Valerie', '(734) 336-2037', 'Michigan'),
     ('Rogers Tami', '(832) 716-9900', 'Texas'),
     ('Ruby Baker', '(630) 651-3872', 'Illinois'),
     ('Spencer Elena', '(787) 427-8126', 'Puerto Rico'),
     ('Wise Lucille', '(351) 441-8184', 'Massachusetts')]

if __name__ == '__main__' :
    unittest.main()
