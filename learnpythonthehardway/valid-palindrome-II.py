# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
#
# Example 1:
# Input: "aba"
# Output: True
# Example 2:
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.
# Note:
# The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
import collections


class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        def isPalindrome(s):
            return s == s[::-1]

        if isPalindrome(s):
            return True
        m = collections.defaultdict(int)
        for c in s:
            m[c] += 1
        cnt, l = 0, ''
        for c in m:
            if m[c] & 1:
                cnt += 1
                l = c
        if cnt > 1:
            return False

        t = ""
        for i in xrange(len(s)):
            if s[i] != l:
                continue
            if i == 0:
                t = s[1:]
            elif i == len(s) - 1:
                t = s[0:i]
            else:
                t = s[0:i] + s[i + 1:]
            if isPalindrome(t):
                return True
        return False


if __name__ == '__main__':
    print Solution().validPalindrome("aba")
    print Solution().validPalindrome("abab")
    print Solution().validPalindrome("abcda")
    print Solution().validPalindrome(
        "llijcmxghaxaqbdoadjclfdcjbulunxbbiknlanbzrlfutqegktxiiylkogzqbhpwcgirtrxedtlqsoiibbxmzfboocrbnvstmvqowjzktkghxiekgudpalsczqhkrssldponbwcvqnieyhbdunpongsmnzuossndmgxllfrudmevvyqethtpehdyknlcpblqnkloakbeikvrhgqirwobwkovcuqxlpfvjhxkpgajnussyuhsqcwwolnpnqyvsyxugqufybhgfwelpcghtsqyrcmfpjqguybmsohivnksyjsykjxipodlhuyeqfsufqovlfxjwlmonflqzrranrrtfduolwrokhagpmanzjzltsyrkjyponzyxlskulnjodjltfvjmdirzpqeyrsddwkagbhbvvswatlwpwbppllcwqcoxnqwfgfafdsndunhpitvxijtczqgtrzkxagdbrfrnhrjwwrnbccmcaaypmwwusomnqrdcmjngwkcpmwkkcgviowuyqkdglfiypdkwvhnssouzuokqmqzzlouaryufuecbkhqmprqiditirkxfehbnurabvxmwuykzhcnhtweeovjybbvtodtjlttmnepvsodnjopoecsjntnnzmjsubvutvjuerfhxjiptpxubjeinovwmdspqrybhmkrwjxlmkrtxtceupincvfbpiwgddjfxrwlmyiekgqzscujmpcmmpdwtzchpocoiperxussepjckyzhzttyjfegdhmskjphsinejhmgdaoeudrsugtbnzxodphwdbededfmciypeurhuykzjkzbcygyobkjesmbmrruvcxvjccryhskzinkioarwqyccdaddasyybrqrybyiajqxqjeyutpppsknxasrrmkestwdxwfqhqaqvjrxdtgoyjhvwpscxypbzbdlnsvdqlzjgjxaxtoxhajtxqpksteieijphgkgtvpcykuwxsogbspqmpvuntyxznwpjhwehcynjqqwajmvqgwhmiqswgwupkofhhgrxmfwippyqjykqiwubcsvtzbkvujmdbcrwqmuaflfujmctbaozuwegzqlqfmlbybgfoooafpjeiticlqfttqxzhqzfioozajjjdktbhiyjkisjydrnbzkpeatjeotiishpxrtkiedapsraznuxmgmrijcrydizqmhmxithxukdzwmxgwrhqdvlqqdhhesaneowplhjnqeevhcmejgzslejhnivuuzftkpnwskpyxlpywqslffvzkvcygncyptosvyyutzcmbfiolchwlpnqeisqngiwkdattkqodpuhlglcawrpnnguyagxdantpmbspvjgcyyihdpygaflonsiatszhmiqvyjbixdjvdtrsvwigvkazwhrcgbyvuofkhaoqysoqpnczwsnrkshriuzztmarupvwasfojvzloqgiuhbngsglzrqcvisqkuarggjlmjwyarkonpoclcikdmpsljbawyajaevbkkammsbripceiwlnnkfrykdfkzvafcallnoehldkboayrwmwxadlmdcrepekxpquhpldgyincdvuxkdpbkfbwfuyvhafogdzswokfuhkwugzizbgskkjmaxynpjqpcxmvsbtiwizgoqivpozbgulannhqgghyrtjsasvqnrhhtvgovkttirrqjreygtzmsvmkkvmxuwjvjggpzviiffjsmghechkmzbslalddbzggvmwhyobgvafqhdmdqatlrilodgjflldvcloyeeswihpvebmnkspzkfwgcoebfpvborkdwtbjbndlgbbaekwdmgzzifvilknthcyfajbkbkqnjljzexfgevxzfnuurvjoxinzdhlfchxylykiizakcsgwuzhxpwptnrctejgyxpgqlzhiklmzheaiudkkdwimlztruhyqznaqqrmierkhwzhmftpzvoeajphhebtgoooouxvtgbejfhfrbfrltuzybcwzhclrswsxnnxrnhypmwmnicvsaudjxdtpgrtwqbseurpronnrvsgqucrimsmkblropmfllecdlyynrcjokgxtkrrvuhgoftdgbycwwwgxdvkykzyjsppwyibiwrqbdsgckbnhqxmtrsxusjhbjbivklyohmnjrlaojfpqraroztrtexlrvrlxszbbbqjiowazmzetxpglirbhcrivxuvplkrwtzgkoewomhvmieqlzcvszmborqcrczbfhiuvmsxhnsrjubkfryhlxedrbwkyecfeefbryktekbfowbjisclbiarhdpzinblbaajzxqeibpbbkiwogrbmyoojvrepevqzftpbievvrqwosyohstkbkaymjqqipxfayctpmamphibdvqenwczyrcwkqetrhvpafswcszoepfkyuatguhdwrznwzysfdyobnnzmciwoslivccdchwssemactnxdhjeipdlqzvuetwvpjrpmcdbmzdaqxbdllxnnymzkgsjukpdqcunekfnvnjsszjsbrefjujtknvlthaetivbihbgbdkoeevmonqoerqmivynrixcwsreocomfmehqamrdxnygyodlvnngshubmuwynseyrevzvuycldrueucarwkyqnyyjwiflvchqcpyrjqfjkzdqgsnflgwcoemnpelhwmrmyqyjdnegxfiyemmzxrprlqgjhyftmyrnlqdzlrhfppdvckgjkvbhwqpcprmtglbfeyfqscffmndeceafzokiepaezvafmkxhadbghecfcshsqwwmomfuisoxkgrutsvbzygkawkvxsxnnzwaekcujyirtblmtzfboiqlskyfnfizwpeeomgbvnwsdzcugrzzixjbdlbvmrvvchquokoqopgzigsaylkrstzxtencexcuapxausfenaiurpfwjxaazivooacrymjtnuqawqwvauvbfhhfntstxgvgnhqhegcstqekkngyeezuwjdcvwxlmdtiwkipdrimsuudlpkdjkczycoutuyysmjhscprtcbdosoalvreufqjmaqfykzczszxhskgdzfbgtzaqrqysrnciipfknxvvkrruuietyqporddniffiqvzsuttgnfyxlnlggvhmeyqqllijxcuigovcoceoxueelbcwjttzkbggtdseyahxwxzwxmrmtbunpopvncjmiieipxhszsntybptibvgbdyahcczkiqtlxxyfxcvwolnubvfxtwufrqxzmgpjecytyfqtmcvqtcdfiwhwbixhtasbfamsmwcybufqcecaptczcxeiefvlkjraxhnshyofwevfdhcxxqlgrskzexfffilnnfmqmwhkgkajytytfrervoxthcmqhgpcxwzxqoxasuomfejjfqtrpvltkmtdticgqebfjoamfdmsfpqyslckygjwbqnszxtpwugpbcsytfioqrggpehkbvgckmtyhjqoofjipcjxrwvbhxktyvgjhyluxvmxmagyhygftgxoshklkuygalbsbeavcyfkwtnmqmzvbtgiiiaphyzsyraqfepbdtqldulsnthxhqvzxiowyqkzqqymajfcqyocqgfmuwglepoacubzmstgpudilyvzqiuqrzrnbuwwfwbclwafrxwccaltjwxvnqgncuhtcolyeneczhikmprolwqoazdjoxmvlixfeyzunnxrknlzilhloegsllheswnbpigbbavlxtehyhoekmgqstsnlfdfojpagoulefmasrmfbppqbjdmjmbtwdmgszsrkhzbrderiokanubsswadfymkqccsthzzrxcvkhvzdbptznbxtoaulsxjmfusujntwewfegfecfdhlcocawdlxeckdtzdsvlhhoniazeeevltmhbxzuzpokoqifytkehthmjdflgixwqtqentvgrhybphugpnikubgklieeprvmjzacwbenyaruddxevoeemeaosrjwuqynvohylapeaeuoiqixpezjrabjjrtyrsltrdxogdnhupormgqlpgzsmapylewztcyubyxavkhegdpukrsrslxkjhtpwgxnlhhmmithluslcbopqppuwmcsaqniabtdhjkfslouqyyhianppnvafnyonoyjxdztazauriggxcrervtkjjoqzwmycquucsdhscegxdopiiqueybcxfwnffhgapiifbmvgsooprzwkbtbplbdwmpkthmsqyazzujjzlynlyhkquxhqtozhgkmlzmuzvdehqmrzwppuwcpwtuhsrfyyjmslpnxiuzkaaxtubxqvngstvckngykqxflayubifehsolxmuhiesvriicawrxrquatgqlvgxckcsquwnncyhwglxzldniqlyxcrybhdqzinorwomftxgmvsdupsptqtgyeworqnioyjbtlrcyikjxbspnwgwrfvlxoyguromgpxziwvrzsavfxlxpzikkmwonxcqflwvespckpbnbffgburhxrrcjsvrjgraeghinmbjzdnykjblxoraigfryntzkhkvxweauoohtfqpectgcpeklmbkispvqordaakcoayzwmymitoqrkleuaimrfgbvkisedwibmlkrtoxopwvtlydjwmfavkdltrruyumnwktsjleeythjnusbqxughrlenporcubuvkrznzkrjibeycuvdsalnrzlcrxlmveccrkljzukkjdymmdvtbtcdnyzicedfwjzpwwytjhoxaoldxaeznsimguthkssauqwzvsgwvtzuhsnahlsshbrwxbyotmviqmhaxrtpwiubvphhfpqauamcinjfaadidlykbqfmkkjurrlypfssbtkwsamveaepoyuwpowsbdhgoemnzajukvfaelebfeufhfrkmwrfgfddiqvjdinkeejhzklwozewgaqhykjegoepqcsukuedxdbjrkptfqjklxpo")