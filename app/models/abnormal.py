#app/models/abnormal
# alert of ids-ac

from app.models import db
class Abnormal(db.Model):

    __tablename__ = 'abnormals'

    id = db.Column(db.Integer, primary_key=True)
    priority = db.Column(db.Integer)
    msg = db.Column(db.String(200))
    classification = db.Column(db.String(100))
    timestamp = db.Column(db.String(60))
    date_time = db.Column(db.String(100),unique=True)
    loc = db.Column(db.String(100))
    country = db.Column(db.String(60))
    src_ip = db.Column(db.String(100))
    src_port = db.Column(db.Integer)
    dst_ip = db.Column(db.String(100))
    dst_port = db.Column(db.Integer)
    duration = db.Column(db.Integer)
    protocol_type = db.Column(db.String(10))
    service = db.Column(db.String(20))
    flag = db.Column(db.String(10))
    src_bytes = db.Column(db.BigInteger)
    dst_bytes = db.Column(db.BigInteger)
    land = db.Column(db.Integer)
    wrong_fragment = db.Column(db.Integer)
    urgent = db.Column(db.BigInteger)
    hot = db.Column(db.Integer)
    count=db.Column(db.Integer)
    srv_count=db.Column(db.Integer)
    serror_rate=db.Column(db.Integer)
    srv_serror_rate=db.Column(db.Integer)
    rerror_rate=db.Column(db.Integer)
    srv_rerror_rate=db.Column(db.Integer)
    same_srv_rate=db.Column(db.Integer)
    diff_srv_rate=db.Column(db.Integer)
    srv_diff_host_rate=db.Column(db.Integer)
    dst_host_count=db.Column(db.Integer)
    dst_host_srv_count=db.Column(db.Integer)
    dst_host_same_srv_rate=db.Column(db.Integer)
    dst_host_diff_srv_rate=db.Column(db.Integer)
    dst_host_same_src_port_rate=db.Column(db.Integer)
    dst_host_srv_diff_host_rate=db.Column(db.Integer)
    dst_host_serror_rate=db.Column(db.Integer)
    dst_host_srv_serror_rate=db.Column(db.Integer)
    dst_host_rerror_rate=db.Column(db.Integer)
    dst_host_srv_rerror_rate=db.Column(db.Integer)

    def __repr__(self):
        return '<Abnormal: {}>'.format(self.name)

                     
    def __init__(self, 
        priority,
        msg,
        classification, 
        timestamp, 
        date_time,
        src_ip,
        src_port,
        dst_ip,
        dst_port,
        duration,
        protocol_type,
        service,
        flag,
        src_bytes,
        dst_bytes,
        land,
        wrong_fragment,
        urgent,
        hot,
        count,
        srv_count,
        serror_rate,
        srv_serror_rate,
        rerror_rate,
        srv_rerror_rate,
        same_srv_rate,
        diff_srv_rate,
        srv_diff_host_rate,
        dst_host_count,
        dst_host_srv_count,
        dst_host_same_srv_rate,
        dst_host_diff_srv_rate,
        dst_host_same_src_port_rate,
        dst_host_srv_diff_host_rate,
        dst_host_serror_rate,
        dst_host_srv_serror_rate,
        dst_host_rerror_rate,
        dst_host_srv_rerror_rate):
        self.priority = priority
        self.msg=msg
        self.classification = classification
        self.timestamp = timestamp
        self.date_time = date_time
        self.src_ip = src_ip
        self.src_port = src_port
        self.dst_ip = dst_ip
        self.dst_port = dst_port
        self.duration = duration
        self.protocol_type = protocol_type
        self.service = service
        self.flag = flag
        self.src_bytes = src_bytes
        self.dst_bytes = dst_bytes
        self.land = land
        self.wrong_fragment = wrong_fragment
        self.urgent = urgent
        self.hot = hot
        self.count=count
        self.srv_count=srv_count
        self.serror_rate=serror_rate
        self.srv_serror_rate=srv_serror_rate
        self.rerror_rate=rerror_rate
        self.srv_rerror_rate=srv_rerror_rate
        self.same_srv_rate=same_srv_rate
        self.diff_srv_rate=diff_srv_rate
        self.srv_diff_host_rate=srv_diff_host_rate
        self.dst_host_count=dst_host_count
        self.dst_host_srv_count=dst_host_srv_count
        self.dst_host_same_srv_rate=dst_host_same_srv_rate
        self.dst_host_diff_srv_rate=dst_host_diff_srv_rate
        self.dst_host_same_src_port_rate=dst_host_same_src_port_rate
        self.dst_host_srv_diff_host_rate=dst_host_srv_diff_host_rate
        self.dst_host_serror_rate=dst_host_serror_rate
        self.dst_host_srv_serror_rate=dst_host_srv_serror_rate
        self.dst_host_rerror_rate=dst_host_rerror_rate
        self.dst_host_srv_rerror_rate=dst_host_srv_rerror_rate

    def update_country(self,loc, country):
        self.loc = loc
        self.country = country

