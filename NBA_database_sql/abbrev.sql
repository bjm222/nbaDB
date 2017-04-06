DROP TABLE IF EXISTS abbrev;
CREATE TABLE abbrev(
   abbrev_type VARCHAR(10) NOT NULL 
  ,code        VARCHAR(3) NOT NULL
  ,full_name   VARCHAR(27) NOT NULL PRIMARY KEY
);
INSERT INTO abbrev(abbrev_type,code,full_name) VALUES ('Round','DF','Division Finals');
INSERT INTO abbrev(abbrev_type,code,full_name) VALUES ('Conference','EC','Eastern Conference');
INSERT INTO abbrev(abbrev_type,code,full_name) VALUES ('Conference','WC','Western Conference');
INSERT INTO abbrev(abbrev_type,code,full_name) VALUES ('Division','AT','Atlantic Division');
INSERT INTO abbrev(abbrev_type,code,full_name) VALUES ('Division','ED','Eastern Division');
INSERT INTO abbrev(abbrev_type,code,full_name) VALUES ('Division','CD','Central Division');
INSERT INTO abbrev(abbrev_type,code,full_name) VALUES ('Division','WD','Western Division');
INSERT INTO abbrev(abbrev_type,code,full_name) VALUES ('Division','SE','Southeast Division');
INSERT INTO abbrev(abbrev_type,code,full_name) VALUES ('Division','MW','Midwest Division');
INSERT INTO abbrev(abbrev_type,code,full_name) VALUES ('Division','NW','Northwest Division');
INSERT INTO abbrev(abbrev_type,code,full_name) VALUES ('Division','SW','Southwest Division');
INSERT INTO abbrev(abbrev_type,code,full_name) VALUES ('Division','PC','Pacific Division');
INSERT INTO abbrev(abbrev_type,code,full_name) VALUES ('Playoffs','R1','Lost round 1');
INSERT INTO abbrev(abbrev_type,code,full_name) VALUES ('Playoffs','SF','Lost semi-finals');
INSERT INTO abbrev(abbrev_type,code,full_name) VALUES ('Playoffs','F','Lost finals');
INSERT INTO abbrev(abbrev_type,code,full_name) VALUES ('Playoffs','NC','Won NBA championship');
INSERT INTO abbrev(abbrev_type,code,full_name) VALUES ('Playoffs','AC','Won ABA championship');
INSERT INTO abbrev(abbrev_type,code,full_name) VALUES ('Playoffs','DT','Lost division tie');
INSERT INTO abbrev(abbrev_type,code,full_name) VALUES ('Playoffs','DF','Lost division finals');
INSERT INTO abbrev(abbrev_type,code,full_name) VALUES ('Playoffs','DS','Lost division semi-finals');
INSERT INTO abbrev(abbrev_type,code,full_name) VALUES ('Playoffs','DR','Lost division round-robin');
INSERT INTO abbrev(abbrev_type,code,full_name) VALUES ('Playoffs','CF','Lost conference finals');
INSERT INTO abbrev(abbrev_type,code,full_name) VALUES ('Playoffs','CS','Lost conference semi-finals');
INSERT INTO abbrev(abbrev_type,code,full_name) VALUES ('Playoffs','C1','Lost conference 1st round');
INSERT INTO abbrev(abbrev_type,code,full_name) VALUES ('Round','DT','Division Tiebreaker');
INSERT INTO abbrev(abbrev_type,code,full_name) VALUES ('Round','DSF','Division Semifinals');
INSERT INTO abbrev(abbrev_type,code,full_name) VALUES ('Round','CF','Conference Finals');
INSERT INTO abbrev(abbrev_type,code,full_name) VALUES ('Round','CFR','Conference First Round');
INSERT INTO abbrev(abbrev_type,code,full_name) VALUES ('Round','CSF','Conference Semifinals');
INSERT INTO abbrev(abbrev_type,code,full_name) VALUES ('Round','RR','Round Robin');
INSERT INTO abbrev(abbrev_type,code,full_name) VALUES ('Round','F','Finals');
INSERT INTO abbrev(abbrev_type,code,full_name) VALUES ('Round','QF','Quarterfinals');
INSERT INTO abbrev(abbrev_type,code,full_name) VALUES ('Round','SF','Semifinals');
INSERT INTO abbrev(abbrev_type,code,full_name) VALUES ('Round','FR','First Round');
INSERT INTO abbrev(abbrev_type,code,full_name) VALUES ('Division','EA','East Division');
INSERT INTO abbrev(abbrev_type,code,full_name) VALUES ('Division','WE','West Division');
INSERT INTO abbrev(abbrev_type,code,full_name) VALUES ('Playoffs','WC','Won Championship');
INSERT INTO abbrev(abbrev_type,code,full_name) VALUES ('Playoffs','LC','Lost Championship');
INSERT INTO abbrev(abbrev_type,code,full_name) VALUES ('Division','SO','South Division');
INSERT INTO abbrev(abbrev_type,code,full_name) VALUES ('Division','NO','North Division');