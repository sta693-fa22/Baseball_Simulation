CREATE TABLE "managershalf" (
    "ID" INTEGER NOT NULL,
    "playerID" VARCHAR(10) NOT NULL,
    "yearID" SMALLINT NOT NULL,
    "teamID" CHARACTER(3) NOT NULL,
    "team_ID" INTEGER NULL,
    "lgID" CHARACTER(2) NULL,
    "inseason" SMALLINT NULL,
    "half" SMALLINT NOT NULL,
    "G" SMALLINT NULL,
    "W" SMALLINT NULL,
    "L" SMALLINT NULL,
    "teamRank" SMALLINT NULL,
    PRIMARY KEY ("ID"),
    FOREIGN KEY("team_ID") REFERENCES "teams" ("ID") ON UPDATE NO ACTION ON DELETE NO ACTION,
    FOREIGN KEY("playerID") REFERENCES "people" ("playerID") ON UPDATE NO ACTION ON DELETE NO ACTION
);