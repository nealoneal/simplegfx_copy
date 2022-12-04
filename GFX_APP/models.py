# models.py root folder
from GFX_APP import db, app

class Project(db.Model):
    __tablename__ = 'projects'
    cis = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.Text)
    producer = db.Column(db.Text)
    name_keys = db.relationship('NameKey', backref='project', lazy='dynamic')
    default_bugs = db.relationship('DefaultBugs', backref='project', uselist=False)
    socials = db.relationship('Socials', backref='project', lazy='dynamic')
    locators = db.relationship('Locators', backref='project', lazy='dynamic')
    slido = db.relationship('Slido', backref='project', lazy='dynamic')
    urls = db.relationship('URLs', backref='project', lazy='dynamic')

    def __int__(self, project_name, producer, cis):
        self.project_name = project_name
        self.producer = producer
        self.cis = cis

    # def gfx_list(self):
    #     report = ""
    #     for namekey in self.name_keys:
    #         report += namekey+"\n"
    #     for bug in self.default_bugs:
    #         report += bug+"\n"
    #     for socials in self.socials:
    #         report += socials + "\n"
    #     for locator in self.slido:
    #         report += locator + "\n"
    #     for event_code in self.slido:
    #         report += f"slido event code: {event_code}" + "\n"
    #     for url in self.urls:
    #         report += url + "\n"
    #     return report

    def __repr__(self):
        return f"CIS: {self.cis} - {self.proj_name}"


class NameKey(db.Model):
    __tablename__ = 'name_keys'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    title = db.Column(db.Text)
    company = db.Column(db.Text)
    cis_id = db.Column(db.Integer, db.ForeignKey('projects.cis'))
    left_aligned = db.Column(db.Integer)
    right_aligned = db.Column(db.Integer)
    otp = db.Column(db.Integer)

    def __int__(self,name, title, company, left_aligned, right_aligned, otp, cis_id):
        self.name = name
        self.title = title
        self.company = company
        self.left_aligned = left_aligned
        self.right_aligned = right_aligned
        self.otp = otp
        self.cis = cis_id

    def __repr__(self):
        left = ""
        right = ""
        otp_text = ""
        if self.left_aligned == 1:
            left = " | Left"
        if self.right_aligned == 1:
            right = " | Right"
        if self.otp == 1:
            otp_text = " | OTP"
        if self.company:
            return f"{self.name}, {self.title}, {self.company}{left}{right}{otp_text}"
        else:
            return f"{self.name}, {self.title}, {left}{right}{otp_text}"


class DefaultBugs(db.Model):
    __tablename__ = 'default_bugs'
    id = db.Column(db.Integer, primary_key=True)
    q_a = db.Column(db.Integer)
    chat = db.Column(db.Integer)
    poll = db.Column(db.Integer)
    survey = db.Column(db.Integer)
    raise_hand = db.Column(db.Integer)
    cis_id = db.Column(db.Integer, db.ForeignKey('projects.cis'))

    def __int__(self, cis):
        self.cis = cis

    # def __repr__(self):
    #
    #     self.q_a = ""
    #     self.chat = ""
    #     self.poll = ""
    #     self.survey = ""
    #     self.raise_hand = ""
    #
    #     if self.q_a == 1:
    #         q_a = " | Q & A"
    #     if self.chat == 1:
    #         chat = " | Chat"
    #     if self.poll == 1:
    #         poll = " | Poll"
    #     if self.survey == 1:
    #         survey = " | Survey"
    #     if self.raise_hand == 1:
    #         raise_hand = " | Raise Hand"
    #     return f"{q_a}, {chat}, {poll}{survey}{raise_hand}"

class Socials(db.Model):
    __tablename__ = 'socials'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    cis_id = db.Column(db.Integer, db.ForeignKey('projects.cis'))

    def __int__(self, cis, text):
        self.cis = cis
        self.text = text

    def __repr__(self):
        return self.text

class Locators(db.Model):
    __tablename__ = 'slido'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    cis_id = db.Column(db.Integer, db.ForeignKey('projects.cis'))

    def __int__(self, cis, text):
        self.cis = cis
        self.text = text

    def __repr__(self):
        return self.text


class Slido(db.Model):
    __tablename__ = 'slido_event_codes'
    id = db.Column(db.Integer, primary_key=True)
    event_code = db.Column(db.Text)
    cis_id = db.Column(db.Integer, db.ForeignKey('projects.cis'))

    def __int__(self, cis, event_code):
        self.cis = cis
        self.event_code = event_code

    def __repr__(self):
        return self.event_code

class URLs(db.Model):
    __tablename__ = 'urls'
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.Text)
    cis_id = db.Column(db.Integer, db.ForeignKey('projects.cis'))

    def __int__(self, cis, url):
        self.cis = cis
        self.url = url

    def __repr__(self):
        return self.url