def fetch_sql1(index):

    stored_query_type1 = [''] * 20
    stored_query_type1[0] = "SELECT DISTINCT pa.first_name, pa.last_name FROM player_allstar pa \
                        WHERE pa.minutes>60 AND  \
                        pa.conference = 'West' AND \
                        pa.season_id > 2000;"
    stored_query_type1[1] = "SELECT DISTINCT pa.first_name, pa.last_name FROM player_allstar pa \
                        WHERE pa.points>30 AND \
                        pa.conference = 'East' AND \
                        pa.season_id > 1998;"
    stored_query_type1[2] = "SELECT DISTINCT pa.first_name, pa.last_name FROM player_allstar pa \
                        WHERE pa.assists>7 AND \
                        pa.conference = 'East' AND \
                        pa.season_id > 1998 AND \
                        pa.personal_fouls<3;"
    stored_query_type1[3] = "SELECT DISTINCT\
                        AVG(res.points) AS pps \
                        FROM \
                        (SELECT DISTINCT \
                        p.year, p.points \
                        FROM \
                        players p, player_allstar pa \
                        WHERE \
                        p.playerID = pa.player_id \
                        AND pa.first_name = 'Kobe' \
                        AND pa.last_name = 'Bryant') AS res;"
    stored_query_type1[4] = "SELECT DISTINCT\
                        AVG(res.assists) AS aPs \
                        FROM \
                        (SELECT DISTINCT \
                        p.year, p.assists \
                        FROM \
                        players p, player_allstar pa \
                        WHERE \
                        p.playerID = pa.player_id \
                        AND pa.first_name = 'Kobe' \
                        AND pa.last_name = 'Bryant' \
                        AND p.year >= 1998 \
                        AND p.year <= 2000) AS res;"
    stored_query_type1[5] = "SELECT DISTINCT\
                        d1.firstName, d1.lastName \
                        FROM \
                        draft d1, \
                        (SELECT \
                        p.playerID, MAX(p.points) \
                        FROM \
                        draft d, players p \
                        WHERE \
                        d.draftYear = 1996 \
                        AND p.playerID = d.playerID \
                        AND p.year = 1996) AS res \
                        WHERE \
                        d1.playerID = res.playerID;"
    stored_query_type1[6] = "SELECT DISTINCT \
                        pa.first_name, pa.last_name \
                        FROM \
                        player_allstar pa, \
                        (SELECT \
                        RES.playerID, MAX(RES.count) \
                        FROM \
                        (SELECT \
                        ap.playerID, COUNT(ap.playerID) AS count \
                        FROM \
                        awards_players ap, (SELECT \
                        RES.playerID \
                        FROM \
                        (SELECT \
                        p.playerID, SUM(p.points) AS total_points \
                        FROM \
                        players p \
                        GROUP BY p.playerID) AS RES \
                        WHERE \
                        RES.total_points > 28000) AS res \
                        WHERE \
                        ap.playerID = res.playerID \
                        AND ap.award = 'All-NBA First Team' \
                        GROUP BY ap.playerID) AS RES) AS RES11 \
                        WHERE \
                        RES11.playerID = pa.player_id;"

    stored_query_type1[7] = "SELECT DISTINCT\
                        d.firstName, d.lastName \
                        FROM \
                        draft d, \
                        (SELECT \
                        p.playerID, MAX(p.points) \
                        FROM \
                        awards_players ap, players p \
                        WHERE \
                        ap.award = 'Rookie of the Year' \
                        AND ap.playerID = p.playerID \
                        AND ap.year = p.year) AS RES \
                        WHERE \
                        d.playerID = RES.playerID;"
    stored_query_type1[8] = "SELECT DISTINCT\
                        d.firstName, d.lastName, \
                        p.threeMade / p.threeAttempted AS Percentage \
                        FROM \
                        draft AS d, \
                        players AS p \
                        WHERE \
                        d.playerID = p.playerID \
                        AND d.firstName = 'Kobe' \
                        AND d.lastName = 'Bryant' \
                        AND p.year = 2011;"
    stored_query_type1[9] = "SELECT DISTINCT\
                        d.firstName, d.lastName, \
                        p.assists / p.GP AS Assists, \
                        p.steals / p.GP AS Steal, \
                        p.points / p.GP AS Points \
                        FROM \
                        players AS p, \
                        draft AS d \
                        WHERE \
                        p.playerID = d.playerID \
                        AND d.firstName = 'Tracy' \
                        AND d.lastName = 'McGrady' \
                        AND p.year = 2005"
    stored_query_type1[10] = "SELECT DISTINCT \
                        d.firstName, d.lastName \
                        FROM \
                        players p, \
                        draft d \
                        WHERE \
                        p.playerID = d.playerID \
                        AND p.tmID IN (SELECT \
                        p2.tmID \
                        FROM \
                        players p2, \
                        draft d2 \
                        WHERE \
                        p2.playerID = d2.playerID \
                        AND p.year = p2.year \
                        AND d2.firstName = 'Yao' \
                        AND d2.lastName = 'Ming')"
    stored_query_type1[11] = "SELECT DISTINCT \
                        d1.firstName, d1.lastName\
                        FROM \
                        players p1, \
                        players p2, \
                        draft d1, \
                        draft d2 \
                        WHERE \
                        p1.playerID = d1.playerID \
                        AND p2.playerID = d2.playerID \
                        AND d2.firstName = 'Yao' \
                        AND d2.lastName = 'Ming' \
                        AND d1.draftYear = d2.draftYear - 1 \
                        AND d1.playerID NOT IN (SELECT \
                        pa.player_id \
                        FROM \
                        player_allstar pa)"
    stored_query_type1[12] = "SELECT DISTINCT \
                        d.firstName, d.lastName \
                        FROM \
                        players p, \
                        draft d \
                        WHERE \
                        p.playerID = d.playerID \
                        AND d.draftYear > 2000 \
                        AND p.playerID IN (SELECT \
                        pa.player_id \
                        FROM \
                        player_allstar pa) \
                        AND EXISTS( SELECT \
                        * \
                        FROM \
                        coaches co, \
                        awards_coaches ac \
                        WHERE \
                        co.coachID = ac.coachID \
                        AND p.tmID = co.tmID \
                        AND p.year = co.year)"
    stored_query_type1[13] = "SELECT DISTINCT \
                        p_a.first_name, p_a.last_name \
                        FROM \
                        player_allstar p_a \
                        WHERE \
                        NOT EXISTS( SELECT \
                        allstar1.season_id \
                        FROM \
                        player_allstar allstar1 \
                        WHERE \
                        allstar1.season_id >= 2003 \
                        AND allstar1.season_id <= 2008 \
                        AND allstar1.season_id NOT IN (SELECT \
                        allstar2.season_id \
                        FROM \
                        player_allstar allstar2 \
                        WHERE \
                        p_a.player_id = allstar2.player_id))"
    stored_query_type1[14] = "SELECT DISTINCT \
                        pa.first_name, pa.last_name\
                        FROM \
                        player_allstar pa \
                        WHERE \
                        NOT EXISTS( SELECT \
                        allstar1.season_id \
                        FROM \
                        player_allstar allstar1 \
                        WHERE \
                        allstar1.first_name = 'Yao' \
                        AND allstar1.last_name = 'Ming' \
                        AND allstar1.season_id NOT IN (SELECT \
                        allstar2.season_id \
                        FROM \
                        player_allstar allstar2 \
                        WHERE \
                        allstar2.player_id = pa.player_id \
                        AND allstar2.player_id != allstar1.player_id))"
    return stored_query_type1[index]

def fetch_sql2(index, fname, lname):

    fname = " '" + fname + "' "
    lname = " '" + lname + "' "

    stored_query_type2 = [''] * 20

    stored_query_type2[0] = "SELECT DISTINCT\
                            d.firstName, d.lastName, p.points / p.GP AS points, p.year \
                            FROM \
                            draft AS d, \
                            players AS p \
                            WHERE \
                            d.playerID = p.playerID \
                            AND d.firstName = " + fname + " \
                            AND d.lastName = " + lname + " \
                            ORDER BY p.year"

    return stored_query_type2[0]

def fetch_sql3(fname, lname):

    fname = " '" + fname + "' "
    lname = " '" + lname + "' "

    stored_query_type3 = [''] * 20

    '''stored_query_type3[0] = "SELECT \
                            d.firstName, d.lastName, p.points / p.GP AS points, p.year \
                            FROM \
                            draft AS d, \
                            players AS p \
                            WHERE \
                            d.playerID = p.playerID \
                            AND d.firstName = " + fname + " \
                            AND d.lastName = " + lname + " \
                            ORDER BY p.year"'''
    stored_query_type3[0] = "SELECT DISTINCT\
                            * \
                            FROM \
                            player_info \
                            WHERE \
                            firstName = " + fname + " \
                            AND lastName = " + lname + " \
                            ORDER BY year;"

    return stored_query_type3[0]

def fetch_sql4(fname, lname):

    fname = " '" + fname + "' "
    lname = " '" + lname + "' "

    stored_query_type4 = [''] * 20

    stored_query_type4[0] = "SELECT DISTINCT\
                            * \
                            FROM \
                            career \
                            WHERE \
                            firstName = " + fname + " \
                            AND lastName = " + lname 
                            
    return stored_query_type4[0]