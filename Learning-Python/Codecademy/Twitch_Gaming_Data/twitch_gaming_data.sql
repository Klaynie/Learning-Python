-- 1
select
	*
from
	stream s
limit 20;

select
	count(*)
from
	stream s; -- 526299

select 
	*
from 
	chat c
limit 20;

select
	count(*)
from
	chat c; -- 148562

-- 2
select
	distinct game
from
	stream s;

-- 3
select
	distinct channel
from
	stream s;


-- 4
select
	s.game,
	count(*)
from
	stream s
group by
	s.game
order by
	2 desc;

-- 5
select
	s.country,
	count(*)
from
	stream s
group by
	s.country
order by
	2 desc;

-- 6
select
	s.player,
	count(*)
from
	stream s
group by
	s.player
order by
	2 desc;

-- 7
select
	s.game,
	case
		when s.game = 'League of Legends' then 'MOBA'
		when s.game = 'Dota 2' then 'MOBA'
		when s.game = 'Heroes of the Storm' then 'MOBA'
		when s.game = 'Counter-Strike: Global Offensive' then 'FPS'
		when s.game = 'DayZ' then 'Survival'
		when s.game = 'ARK: Survival Evolved' then 'Survival'
		else 'Other'
	end as genre
from
	stream s
group by 1
order by 2;


-- 8
select
	s.time
from
	stream s
limit 10;

-- 9
select
	s.time,
	strftime('%S', s.time)
from
	stream s
group by
	1
limit 20;

-- 10
select
	strftime('%H', s.time),
	count(*)
from
	stream s
where
	s.country = 'US'
group by
	1
order by
	1;

-- 11
select
	*
from
	stream s
join chat c 
on
	c.device_id = s.device_id; 