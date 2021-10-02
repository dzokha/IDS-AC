#app/models/alert
# alert of snort

from app.models import db

class Alert(db.Model):

    __tablename__ = 'alerts'

    id = db.Column(db.Integer, primary_key=True)
    gid_sid_rev = db.Column(db.String(20))
    msg = db.Column(db.String(200))
    classification = db.Column(db.String(100))
    priority = db.Column(db.Integer)
    timestamp = db.Column(db.String(60))
    date_time = db.Column(db.String(100),unique=True)
    loc = db.Column(db.String(100))
    country = db.Column(db.String(60))
    src_ip = db.Column(db.String(100))
    src_port = db.Column(db.Integer)
    dst_ip = db.Column(db.String(100))
    dst_port = db.Column(db.Integer)
    meta_data = db.Column(db.String(500))

    def __repr__(self):
        return '<Alert: {}>'.format(self.name)

    def __init__(self, gid_sid_rev, msg, classification, priority, timestamp, date_time,src_ip,src_port,dst_ip,dst_port,meta_data):
        self.gid_sid_rev = gid_sid_rev
        self.msg = msg
        self.classification = classification
        self.priority = priority
        self.timestamp = timestamp
        self.date_time = date_time
        self.src_ip = src_ip
        self.src_port = src_port
        self.dst_ip = dst_ip
        self.dst_port = dst_port
        self.meta_data = meta_data


    def update_country(self,loc, country):
        self.loc = loc
        self.country = country

# class Alert_file(db.Model):

#     __tablename__ = 'alert_files'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(60))
#     description = db.Column(db.String(200))

#     def __repr__(self):
#         return '<Alert_file: {}>'.format(self.name)

#     def __init__(self, name, description):
#         self.name = name
#         self.description = description

# class Csv_file(db.Model):

#     __tablename__ = 'csv_files'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(60))
#     description = db.Column(db.String(200))

#     def __repr__(self):
#         return '<Csv_file: {}>'.format(self.name)

#     def __init__(self, name, description):
#         self.name = name
#         self.description = description

# class Deepmg_file(db.Model):

#     __tablename__ = 'deepmg_files'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(60))
#     description = db.Column(db.String(200))

#     def __repr__(self):
#         return '<Deepmg_file: {}>'.format(self.name)

#     def __init__(self, name, description):
#         self.name = name
#         self.description = description



# class Tcpdump_file(db.Model):

#     __tablename__ = 'tcpdump_files'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(60))
#     description = db.Column(db.String(200))

#     def __repr__(self):
#         return '<Tcpdump_file: {}>'.format(self.name)

#     def __init__(self, name, description):
#         self.name = name
#         self.description = description


# class Data_attack(db.Model):

#     __tablename__ = 'data_attacks'

#     id = db.Column(db.Integer, primary_key=True)    
#     duration = db.Column(db.Integer)
#     protocol_type = db.Column(db.String(60))
#     service = db.Column(db.String(60))
#     flag = db.Column(db.String(60))
#     src_bytes = db.Column(db.Float)
#     dst_bytes = db.Column(db.Float)
#     land = db.Column(db.Float)
#     wrong_fragment = db.Column(db.Float)
#     urgent = db.Column(db.Float)
#     hot = db.Column(db.Float)
#     count = db.Column(db.Float)
#     srv_count = db.Column(db.Float)
#     serror_rate = db.Column(db.Float)
#     srv_serror_rate = db.Column(db.Float)
#     rerror_rate = db.Column(db.Float)
#     srv_rerror_rate = db.Column(db.Float)
#     same_srv_rate = db.Column(db.Float)
#     diff_srv_rate = db.Column(db.Float)
#     srv_diff_host_rate = db.Column(db.Float)
#     dst_host_count = db.Column(db.Float)
#     dst_host_srv_count = db.Column(db.Float)
#     dst_host_same_srv_rate = db.Column(db.Float)
#     dst_host_diff_srv_rate = db.Column(db.Float)
#     dst_host_same_src_port_rate = db.Column(db.Float)
#     dst_host_srv_diff_host_rate = db.Column(db.Float)
#     dst_host_serror_rate = db.Column(db.Float)
#     dst_host_srv_serror_rate = db.Column(db.Float)
#     dst_host_rerror_rate = db.Column(db.Float)
#     dst_host_srv_rerror_rate = db.Column(db.Float)
#     ip_id = db.Column(db.Float)
#     ip_proto = db.Column(db.Float)
#     tcp_seq = db.Column(db.Float)
#     tcp_flag = db.Column(db.Float)
#     src_ip = db.Column(db.String(60))
#     src_port = db.Column(db.Float)
#     dst_ip = db.Column(db.String(60))
#     dst_port = db.Column(db.Float)
#     udp_length = db.Column(db.Float)
#     frame_length = db.Column(db.Float)  
#     geo_country = db.Column(db.String(60))
#     data = db.Column(db.String(200))
#     timestamp = db.Column(db.String(60))
#     date_time = db.Column(db.String(100))


#     def __repr__(self):
#         return '<Data_attack: {}>'.format(self.name)

#     def __init__(self, duration, protocol_type, service, flag, src_bytes, dst_bytes, land, wrong_fragment, urgent, hot, count, srv_count, serror_rate, srv_serror_rate, rerror_rate, srv_rerror_rate, same_srv_rate, diff_srv_rate, srv_diff_host_rate, dst_host_count, dst_host_srv_count, dst_host_same_srv_rate, dst_host_diff_srv_rate, dst_host_same_src_port_rate, dst_host_srv_diff_host_rate, dst_host_serror_rate, dst_host_srv_serror_rate, dst_host_rerror_rate, dst_host_srv_rerror_rate, ip_id, ip_proto, tcp_seq, tcp_flag, src_ip, src_port, dst_ip, dst_port, udp_length, frame_length, geo_country, data, timestamp, date_time):
#         self.duration = duration
#         self.protocol_type = protocol_type
#         self.service = service
#         self.flag = flag
#         self.src_bytes = src_bytes
#         self.dst_bytes = dst_bytes
#         self.land = land 
#         self.wrong_fragment = wrong_fragment
#         self.urgent = urgent
#         self.hot = hot
#         self.count = count
#         self.srv_count = srv_count
#         self.serror_rate = serror_rate
#         self.srv_serror_rate = srv_serror_rate
#         self.rerror_rate = rerror_rate
#         self.srv_rerror_rate = srv_rerror_rate
#         self.same_srv_rate = same_srv_rate
#         self.diff_srv_rate = diff_srv_rate
#         self.srv_diff_host_rate = srv_diff_host_rate
#         self.dst_host_count = dst_host_count
#         self.dst_host_srv_count = dst_host_srv_count
#         self.dst_host_same_srv_rate = dst_host_same_srv_rate
#         self.dst_host_diff_srv_rate = dst_host_diff_srv_rate
#         self.dst_host_same_src_port_rate = dst_host_same_src_port_rate
#         self.dst_host_srv_diff_host_rate = dst_host_srv_diff_host_rate
#         self.dst_host_serror_rate = dst_host_serror_rate
#         self.dst_host_srv_serror_rate = dst_host_srv_serror_rate
#         self.dst_host_rerror_rate = dst_host_rerror_rate
#         self.dst_host_srv_rerror_rate = dst_host_srv_rerror_rate
#         self.ip_id = ip_id
#         self.ip_proto = ip_proto
#         self.tcp_seq = tcp_seq
#         self.tcp_flag = tcp_flag
#         self.src_ip = src_ip
#         self.src_port = src_port
#         self.dst_ip = dst_ip
#         self.dst_port = dst_port
#         self.udp_length = udp_length
#         self.frame_length = frame_length
#         self.geo_country = geo_country
#         self.data = data
#         self.timestamp = timestamp
#         self.date_time = date_time



    

