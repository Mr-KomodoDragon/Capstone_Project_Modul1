# Latihan 3 SQL: Sub-Query dan Join
# Database: world

# JOIN
# 1. Tampilkan 10 kota dengan populasi terbesar beserta nama negaranya, urutkan berdasarkan
# populasinya dari yang terbesar!

select ci.Name as nama_kota, co.Name as negara, ci.Population
from country co
join city ci
on co.Code = ci.CountryCode
order by ci.Population desc
limit 10;

# 2. Tampikan GNP negara Belanda (Netherlands), ibukota, beserta populasi dari ibukotanya!
Select co.Name as Negara, co.GNP as GNP, ci.Name as Capital, co.Population
from country co
join city ci
on co.Code= ci.CountryCode
where co.Name = 'Netherlands' and ci.Name = 'Amsterdam';

# 3. Tampilkan 10 negara yang memiliki persentase pemakai bahasa spanyol paling tinggi!
select co.Name As Negara, cl.Percentage as Presentase
from country co
join countrylanguage cl
on co.Code = cl.CountryCode
where cl.language = 'spanish'
order by Presentase DESC;

# 4. Tampikan GNP negara Indonesia, ibukota, populasi dari ibukotanya dan bahasa resmi yang
# dipakai!

select co.Name as Negara, round(co.GNP,1 ) as GNP, ci.Name as Ibu_Kota, cl.Language as Bahasa
from country co join countrylanguage cl join city ci
on co.code = ci.CountryCode and ci.CountryCode = cl.CountryCode
where co.name = 'Indonesia' and cl.Language = 'Malay' and ci.Name = 'Jakarta';

#SubQuery
# 1. Tampilkan benua dengan jumlah negara lebih dari jumlah negara di benua North America!
select count(name) from country
where continent = 'North America';

select continent, count(Name) as Jumlah_Negara from country
group by continent
Having Jumlah_Negara > (select count(name) from country
where continent = 'North America');

# 2. Tampilkan negara di Asia dengan GNP di atas rata-rata GNP negara-negara di benua Eropa,
# diurutkan dari yang terbesar!
select round(avg(GNP),1) from country
where continent = 'Europe';

select Name,GNP from country
where Continent = 'Asia' and GNP >(select round(avg(GNP),1) from country
where continent = 'Europe')
order by GNP desc;

# 3. Tampilkan benua berakhiran huruf 'a' dengan jumlah region lebih dari jumlah region benua
# Asia!
select count(distinct region) from country
where continent ='asia';

select count(distinct region), continent from country
group by continent
having count(distinct region) > (select count(distinct region) from country
where continent ='asia') and Continent Like '%a';