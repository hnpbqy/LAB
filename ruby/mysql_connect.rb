require "mysql"
dbc = Mysql.real_connect('127.0.0.1','root','123','test')
res = dbc.query('select * from users')
while row = res.fetch_row do
  puts "#{row[0]},#{row[1]}"
end
