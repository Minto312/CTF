intext = "aaa'#"


start = "*}}) RETURN n'\#"
end = '2'
query = f'MATCH (n {{id: {start}}})-[p *bfs]-(m {{id: {end}}}) RETURN size(p) AS distance;'
print(query)

e='}FTC_3h7_y0jn3-!d3s54P_kc3hC_y71n4S{LTBT'
print(e[::-1])