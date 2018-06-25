from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("http://dbpedia.org/sparql")

def getInitResult() :
    name = "月球"
    sparql.setQuery("""
       PREFIX dbo: <http://dbpedia.org/ontology/>
    	PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    	PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    	PREFIX dct: <http://purl.org/dc/terms/>

    	SELECT distinct ?movie ?name ?subject ?thumnail ?abstract
        WHERE
        {
            ?movie rdf:type dbo:Film.
            ?movie rdfs:label ?name.
            ?movie dbo:abstract ?abstract.
            OPTIONAL{
    			?movie dbo:thumbnail ?thumnail.
            } 
            ?movie dct:subject ?subject.
            FILTER(REGEX(?name,"%s","i")).
        } 
        ORDER BY DESC(?movie)
        limit 5
    """%name)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    return results

if __name__ == '__main__':
    results = getInitResult()
    print(results)
    for result in results["results"]["bindings"]:
        print(result["movie"]["value"])
        print(result["name"]["value"])
        #print(result["thumbnail"]["value"])
        print(result["subject"]["value"])
        print(result["abstract"]["value"])