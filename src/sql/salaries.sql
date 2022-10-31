CREATE TABLE "salaries" (
    "ID" INTEGER NOT NULL,
    "yearID" SMALLINT NOT NULL,
    "teamID" CHARACTER(3) NOT NULL,
    "team_ID" INTEGER NULL,
    "lgID" CHARACTER(2) NOT NULL,
    "playerID" VARCHAR(9) NOT NULL,
    "salary" DOUBLE NULL,
    PRIMARY KEY ("ID"),
    FOREIGN KEY("team_ID") REFERENCES "teams" ("ID") ON UPDATE NO ACTION ON DELETE NO ACTION,
    FOREIGN KEY("playerID") REFERENCES "people" ("playerID") ON UPDATE NO ACTION ON DELETE NO ACTION
);