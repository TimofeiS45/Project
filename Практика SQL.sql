Insert into Proizvoditeli values 
(21701, 'Samsung', '���������')
Insert into Pereferia values 
(6,21701, '������� ��������', '������', '���', 17000)

select Proizvoditeli.������, �����, ������������ from Proizvoditeli inner join Pereferia on Proizvoditeli.������ = Pereferia.������ order by �����

select * from Proizvoditeli where ��������� = '��' order by ����� 
select count(������), ����� from Proizvoditeli group by �����

select * from PK where ���� < 35000 order by ����

select ���� from PK
update PK set ���� =(����*1.07)
select ���� from PK

select * from Pereferia where ���� between 3000 and 5500

select * from Proizvoditeli inner join Pereferia on Proizvoditeli.������ = Pereferia.������ where (����� = 'Samsung' or ����� ='Espon') and ������������ = '������� ��������' or ������������ = '������� ��������'

select Proizvoditeli.������, ����� from  Proizvoditeli inner join Pereferia on Proizvoditeli.������ = Pereferia.������ where ���� < 7000 and ��������� = '�������'

select min(����) from Pereferia where ������������ = '����'

select * from PK inner join Proizvoditeli on PK.������ = Proizvoditeli.������ where ������������ = '��������' and ����� = 'Lenovo'
 
 select min(����) from PK where HDD > 130 and RAM = 8