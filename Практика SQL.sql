Insert into Proizvoditeli values 
(21701, 'Samsung', 'Переферия')
Insert into Pereferia values 
(6,21701, 'Принтер лазерный', 'Вывода', 'Зел', 17000)

select Proizvoditeli.Модель, Марка, Наименование from Proizvoditeli inner join Pereferia on Proizvoditeli.Модель = Pereferia.Модели order by Марка

select * from Proizvoditeli where ТипТовара = 'ПК' order by Марка 
select count(Модель), Марка from Proizvoditeli group by Марка

select * from PK where Цена < 35000 order by Цена

select Цена from PK
update PK set Цена =(Цена*1.07)
select Цена from PK

select * from Pereferia where Цена between 3000 and 5500

select * from Proizvoditeli inner join Pereferia on Proizvoditeli.Модель = Pereferia.Модели where (Марка = 'Samsung' or Марка ='Espon') and Наименование = 'Принтер лазерный' or Наименование = 'Принтер струйный'

select Proizvoditeli.Модель, Марка from  Proizvoditeli inner join Pereferia on Proizvoditeli.Модель = Pereferia.Модели where Цена < 7000 and Цветность = 'Цветной'

select min(Цена) from Pereferia where Наименование = 'Мышь'

select * from PK inner join Proizvoditeli on PK.Модели = Proizvoditeli.Модель where Наименование = 'Моноблок' and Марка = 'Lenovo'
 
 select min(Цена) from PK where HDD > 130 and RAM = 8