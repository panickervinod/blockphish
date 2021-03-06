import unittest
import sys
sys.path.append('../')
import blockphish

class test_main(unittest.TestCase):
    
    def test_score_domain(self):

        domain = "paypal.com"
        watch_domain = "paypal.com"
        score = blockphish.score_domain(domain, watch_domain, {})
        print ("Domain: {} Watch Domain: {} Score: {}".format(domain, watch_domain, score))
        self.assertEqual(score, 0, "paypal.com is the watch domain and paypal.com is the suspect domain. Shouldn't flag")
        
        # Check for the domain in the watch_domain
        domain = "paypal.com.paypel.com"
        watch_domain = "paypal.com"
        score = blockphish.score_domain(domain, watch_domain, {})
        print ("Domain: {} Watch Domain: {} Score: {}".format(domain, watch_domain, score))
        self.assertGreaterEqual(score, 100, "domain in the watch_domain not flagging")

        # Check for simple typo
        domain = "paypel1.com"
        watch_domain = "paypal.com"
        score = blockphish.score_domain(domain, watch_domain, {})
        print ("Domain: {} Watch Domain: {} Score: {}".format(domain, watch_domain, score))
        self.assertGreater(score, 60, "domain in the watch_domain not flagging")

        # Check for simple typo
        domain = "paypel.com"
        watch_domain = "paypal.com"
        score = blockphish.score_domain(domain, watch_domain, {})
        print ("Domain: {} Watch Domain: {} Score: {}".format(domain, watch_domain, score))
        self.assertGreater(score, 60, "domain in the watch_domain not flagging")

        # Check for different TLD
        domain = "paypal.net"
        watch_domain = "paypal.com"
        score = blockphish.score_domain(domain, watch_domain, {})
        print ("Domain: {} Watch Domain: {} Score: {}".format(domain, watch_domain, score))
        self.assertGreater(score, 80, "domain in the watch_domain not flagging")
        
        # Check for keywords
        domain = "test.my.paypal.domain.com"
        watch_domain = "paypal.com"
        score = blockphish.score_domain(domain, watch_domain, {'paypal':80})
        print ("Domain: {} Watch Domain: {} Score: {}".format(domain, watch_domain, score))
        self.assertGreaterEqual(score, 80, "domain in the watch_domain not flagging")
        
        # Check that keywords don't get valued too much
        domain = "test.my.paypal.domain.com"
        watch_domain = "porpoise.com"
        score = blockphish.score_domain(domain, watch_domain, {'paypal':100})
        print ("Domain: {} Watch Domain: {} Score: {}".format(domain, watch_domain, score))
        self.assertLess(score, 60, "domain in the watch_domain not flagging")
        
        # Check for keywords
        domain = "test.my.paypel.domain.com.co.za"
        watch_domain = "paypal.com"
        score = blockphish.score_domain(domain, watch_domain, {'paypal':80})
        print ("Domain: {} Watch Domain: {} Score: {}".format(domain, watch_domain, score))
        self.assertGreater(score, 70, "domain in the watch_domain not flagging")
       
        # Check for keywords
        domain = "test.my.paypel-domain.com.co.za"
        watch_domain = "paypal.com"
        score = blockphish.score_domain(domain, watch_domain, {'paypal':100})
        print ("Domain: {} Watch Domain: {} Score: {}".format(domain, watch_domain, score))
        self.assertGreater(score, 70, "domain in the watch_domain not flagging")
        
        # Check for keywords
        domain = "hpay.info"
        watch_domain = "paypal.com"
        score = blockphish.score_domain(domain, watch_domain, {'paypal':75, 'paypalcorp':50})
        print ("Domain: {} Watch Domain: {} Score: {}".format(domain, watch_domain, score))
        self.assertLess(score, 60, "domain in the watch_domain not flagging")
        
        # Check for unicode
        domain = "test.my.pӓypӓl-domӓin.com.co.za"
        watch_domain = "paypal.com"
        score = blockphish.score_domain(domain, watch_domain, {'test.my.paypel-domain.com.co.za':0})
        print ("Domain: {} Watch Domain: {} Score: {}".format(domain, watch_domain, score))
        self.assertGreater(score, 100, "domain in the watch_domain not flagging")
        
        # Check for similar but longer
        domain = "pay-pal.com"
        watch_domain = "paypal.com"
        score = blockphish.score_domain(domain, watch_domain, {'paypal':80})
        print ("Domain: {} Watch Domain: {} Score: {}".format(domain, watch_domain, score))
        self.assertGreater(score, 50, "domain in the watch_domain not flagging")

        # Check for similar but longer
        domain = "ilovepaypal.com"
        watch_domain = "paypal.com"
        score = blockphish.score_domain(domain, watch_domain, {'paypal':80})
        print ("Domain: {} Watch Domain: {} Score: {}".format(domain, watch_domain, score))
        self.assertGreater(score, 60, "domain in the watch_domain not flagging")

        # Check for similar but longer
        domain = "paypal.com"
        watch_domain = "ilovepaypal.com"
        score = blockphish.score_domain(domain, watch_domain, {'paypal':80})
        print ("Domain: {} Watch Domain: {} Score: {}".format(domain, watch_domain, score))
        self.assertGreater(score, 60, "domain in the watch_domain not flagging")
        
        # Check for no match
        domain = "johnsapples.com"
        watch_domain = "paypal.com"
        score = blockphish.score_domain(domain, watch_domain, {'asdfaaadsf':80})
        print ("Domain: {} Watch Domain: {} Score: {}".format(domain, watch_domain, score))
        self.assertLess(score, 50, "domain in the watch_domain not flagging")

        # Check for no match
        domain = "whiteoleanderphotography.com"
        watch_domain = "myetherwallet.com"
        score = blockphish.score_domain(domain, watch_domain, {'asdfaaadsf':80})
        print ("Domain: {} Watch Domain: {} Score: {}".format(domain, watch_domain, score))
        self.assertLess(score, 50, "domain in the watch_domain not flagging")

        # Check for no match
        domain = "subdomain.whiteoleanderphotography.com"
        watch_domain = "myetherwallet.com"
        score = blockphish.score_domain(domain, watch_domain, {'asdfaaadsf':80})
        print ("Domain: {} Watch Domain: {} Score: {}".format(domain, watch_domain, score))
        self.assertLess(score, 50, "domain in the watch_domain not flagging")

        # Check for no match
        domain = "shuswapconcretefinishing.com"
        watch_domain = "wacoin.com"
        score = blockphish.score_domain(domain, watch_domain, {'asdfaaadsf':80})
        print ("Domain: {} Watch Domain: {} Score: {}".format(domain, watch_domain, score))
        self.assertLess(score, 50, "domain in the watch_domain not flagging")

        # Check for no match
        domain = "www.shuswapconcretefinishing.com"
        watch_domain = "wacoin.com"
        score = blockphish.score_domain(domain, watch_domain, {'asdfaaadsf':80})
        print ("Domain: {} Watch Domain: {} Score: {}".format(domain, watch_domain, score))
        self.assertLess(score, 50, "domain in the watch_domain not flagging")
        
        # Check for no match
        domain = "www.blockchainrc.info"
        watch_domain = "myetherwallet.com"
        score = blockphish.score_domain(domain, watch_domain, {'asdfaaadsf':80})
        print ("Domain: {} Watch Domain: {} Score: {}".format(domain, watch_domain, score))
        self.assertLess(score, 50, "domain in the watch_domain not flagging")

        # Check for no match
        domain = "www.upkayak.com"
        watch_domain = "paypal.com"
        score = blockphish.score_domain(domain, watch_domain, {'asdfaaadsf':80})
        print ("Domain: {} Watch Domain: {} Score: {}".format(domain, watch_domain, score))
        self.assertLess(score, 70, "domain in the watch_domain not flagging")
        
        # Check for no match
        domain = "experiencemastercraft.com"
        watch_domain = "paypal.com"
        score = blockphish.score_domain(domain, watch_domain, {'asdfaaadsf':80})
        print ("Domain: {} Watch Domain: {} Score: {}".format(domain, watch_domain, score))
        self.assertLess(score, 50, "domain in the watch_domain not flagging")

        # Check for no match
        domain = "5era.com"
        watch_domain = "myetherwallet.com"
        score = blockphish.score_domain(domain, watch_domain, {'asdfaaadsf':80})
        print ("Domain: {} Watch Domain: {} Score: {}".format(domain, watch_domain, score))
        self.assertLess(score, 50, "domain in the watch_domain not flagging")

        # Check for no match
        domain = "ethereal.hr"
        watch_domain = "myetherwallet.com"
        score = blockphish.score_domain(domain, watch_domain, {'asdfaaadsf':80})
        print ("Domain: {} Watch Domain: {} Score: {}".format(domain, watch_domain, score))
        self.assertLess(score, 90, "domain in the watch_domain not flagging")

        # Check for no match
        domain = "www.fencecompanyplanotx.com"
        watch_domain = "myetherwallet.com"
        score = blockphish.score_domain(domain, watch_domain, {'asdfaaadsf':80})
        print ("Domain: {} Watch Domain: {} Score: {}".format(domain, watch_domain, score))
        self.assertLess(score, 40, "domain in the watch_domain not flagging")

        # Check for no match
        domain = "caspar.one"
        watch_domain = "paypal.com"
        score = blockphish.score_domain(domain, watch_domain, {'paypal':75, 'paypalcorp': 50})
        print ("Domain: {} Watch Domain: {} Score: {}".format(domain, watch_domain, score))
        self.assertLess(score, 50, "domain in the watch_domain not flagging")

        # Check for no match
        domain = "psymap.ga"
        watch_domain = "paypal.com"
        score = blockphish.score_domain(domain, watch_domain, {'paypal':75, 'paypalcorp': 50})
        print ("Domain: {} Watch Domain: {} Score: {}".format(domain, watch_domain, score))
        self.assertLess(score, 50, "domain in the watch_domain not flagging")
       
        domain = "Thṛomas.ga"
        watch_domain = "paypal.com"
        score = blockphish.score_domain(domain, watch_domain, {'paypal':75, 'paypalcorp': 50})
        print ("Domain: {} Watch Domain: {} Score: {}".format(domain, watch_domain, score))
        self.assertLess(score, 50, "domain in the watch_domain not flagging")
       
        
def main():
    unittest.main()


if __name__ == '__main__':
    main()
