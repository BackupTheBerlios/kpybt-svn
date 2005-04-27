from qt import QString
from kdecore import *

class KPyBTMySettings(KConfigSkeleton):
    def __init__(self):
        KConfigSkeleton.__init__(self)
        # Globals
        self.TorrentDirectory=QString("")
        self.DownloadDirectory=QString("")
        self.TorrentDeleteAfterStop=bool(1)
        self.DeleteDatafileAfterStop=bool(0)
        self.DeleteTorrentAndDataFileAfterStop=bool(0)
        self.TorrentStartImmediatly=bool(0)
        self.TorrentRemoveFromListAfterFinish=bool(1)
        
        # Network
        self.BindIP=QString("000.000.000.000")
        self.HTTPTimeout=60
        self.KeepaliveInterval=120
        # Global
        self.setCurrentGroup('Global')
        self.addItemPath("TorrentDirectory",self.TorrentDirectory,QString("/home/shermann"))
        self.addItemPath("DownloadDirectory",self.DownloadDirectory,QString("/home/shermann"))
        self.addItemBool("TorrentDeleteAfterStop",self.TorrentDeleteAfterStop)
        self.addItemBool("DeleteDatafileAfterStop",self.DeleteDatafileAfterStop)
        self.addItemBool("DeleteTorrentAndDataFileAfterStop",self.DeleteTorrentAndDataFileAfterStop)
        self.addItemBool("TorrentStartImmediatly",self.TorrentStartImmediatly)
        self.addItemBool("TorrentRemoveFromListAfterFinish",self.TorrentRemoveFromListAfterFinish)
        self.setCurrentGroup('Network')
        self.addItemString("BindIP",self.BindIP,QString(""))
        self.addItemInt("HttpTimeout",self.HTTPTimeout)
        self.addItemInt("KeepaliveInterval",self.KeepaliveInterval)

#defaults = [
#    ('max_uploads', 7,
#        "the maximum number of uploads to allow at once."),
#    ('keepalive_interval', 120.0,
#        'number of seconds to pause between sending keepalives'),
#    ('download_slice_size', 2 ** 14,
#        "How many bytes to query for per request."),
#    ('request_backlog', 5,
#        "how many requests to keep in a single pipe at once."),
#    ('max_message_length', 2 ** 23,
#        "maximum length prefix encoding you'll accept over the wire - larger values get the connection dropped."),
#    ('ip', '',
#        "ip to report you have to the tracker."),
#    ('minport', 6881, 'minimum port to listen on, counts up if unavailable'),
#    ('maxport', 6999, 'maximum port to listen on'),
#    ('responsefile', '',
#        'file the server response was stored in, alternative to url'),
#    ('url', '',
#        'url to get file from, alternative to responsefile'),
#    ('saveas', '',
#        'local file name to save the file as, null indicates query user'),
#    ('timeout', 300.0,
#        'time to wait between closing sockets which nothing has been received on'),
#    ('timeout_check_interval', 60.0,
#        'time to wait between checking if any connections have timed out'),
#    ('max_slice_length', 2 ** 17,
#        "maximum length slice to send to peers, larger requests are ignored"),
#    ('max_rate_period', 20.0,
#        "maximum amount of time to guess the current rate estimate represents"),
#    ('bind', '', ok
#        'ip to bind to locally'),
#    ('upload_rate_fudge', 5.0,
#        'time equivalent of writing to kernel-level TCP buffer, for rate adjustment'),
#    ('display_interval', .5,
#        'time between updates of displayed information'),
#    ('rerequest_interval', 5 * 60,
#        'time to wait between requesting more peers'),
#    ('min_peers', 20,
#        'minimum number of peers to not do rerequesting'),
#    ('http_timeout', 60,
#        'number of seconds to wait before assuming that an http connection has timed out'),
#    ('max_initiate', 35,
#        'number of peers at which to stop initiating new connections'),
#    ('max_allow_in', 55,
#        'maximum number of connections to allow, after this new incoming connections will be immediately closed'),
#      ('check_hashes', 1,
#        'whether to check hashes on disk'),
#    ('max_upload_rate', 0,
#        'maximum kB/s to upload at, 0 means no limit'),
#    ('snub_time', 30.0,
#        "seconds to wait for data to come in over a connection before assuming it's semi-permanently choked"),
 #   ('spew', 0,
#        "whether to display diagnostic info to stdout"),
#    ('rarest_first_cutoff', 4,
#        "number of downloads at which to switch from random to rarest first"),
#    ('min_uploads', 4,
#        "the number of uploads to fill out to with extra optimistic unchokes"),
#    ('report_hash_failures', 0,
#        "whether to inform the user that hash failures occur. They're non-fatal."),
#    ]
        
