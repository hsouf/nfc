

import nfc
import sys


clf = nfc.ContactlessFrontend('usb')


def load_tag(batchId):
    """ try:
        self.options.data
    except AttributeError:
        try:
            self.options.data = self.options.input.buffer.read()
        except AttributeError:
            self.options.data = self.options.input.read()
        try:
            self.options.data = binascii.unhexlify(self.options.data)
        except binascii.Error:
            pass """

    f = open(batchId+'.txt', 'w')

    """ logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
    file_handler = logging.FileHandler(batchId+'-logs.log')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter) """

    # logger.addHandler(file_handler)
    # print("hello")

    while True:

        tag = clf.connect(rdwr={'on-connect': lambda tag: False})
        #randomHash = uuid.uuid4().hex
        # f.write("http://troof.io/A002"+randomHash+"\n")
        #os.system('python3 hello.py hello')

        if tag.ndef is None:
            print("This is not an NDEF Tag.")

        if not tag.ndef.is_writeable:
            print("This Tag is not writeable.")

        # if options.data == tag.ndef.octets:
            #print("The Tag already contains the message to write.")

        """ if len(data) > tag.ndef.capacity:
            print("The new message exceeds the Tag's capacity.") """

        if tag.ndef.length > 0:
            print("Current NDEF Message:")
            for i, record in enumerate(tag.ndef.records):
                print("record", i + 1)
                print("  type =", repr(record.type))
                print("  name =", repr(record.name))
                print("  data =", repr(record.data))
                print("  uri =", repr(record.uri))
        if tag.ndef.length == 0:
            print("Current NDEF Message:")
            print("EMPTY TAG")


load_tag(sys.argv[1])
