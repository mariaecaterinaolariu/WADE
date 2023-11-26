using Lucene.Net.Search;
using System.Text;
using VDS.RDF;
using VDS.RDF.Parsing;
using VDS.RDF.Query;
using WebApplication1.Repositories;

namespace WebApplication1.Service
{
    public class ImageService : IImageService
    {
        //private readonly IImageRepository _imageRepository;
        public ImageService() {
        }

        public IEnumerable<Dictionary<string, string>> GetImageInformation()
        {
            RdfHelper.SaveAsRDF();
            var rdf = File.ReadAllText("Files\\output.rdf", Encoding.UTF8);
            var graph = new Graph();
            FileLoader.Load(graph, "Files\\output.rdf");

            var query = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\r\nPREFIX ex: <http://example.org/>\r\n\r\nSELECT ?age ?x ?y ?w ?h ?dominant_gender ?Woman ?Man ?dominant_race ?asian ?indian ?black ?white ?middle_eastern ?latino_hispanic ?dominant_emotion ?angry ?disgust ?fear ?happy ?sad ?surprise ?neutral\r\nWHERE {\r\n  ?individual rdf:type ex:Individual ;\r\n              ex:age ?age ;\r\n              ex:region ?region ;\r\n              ex:dominant_gender ?dominant_gender ;\r\n              ex:gender ?gender ;\r\n              ex:dominant_race ?dominant_race ;\r\n              ex:race ?race ;\r\n              ex:dominant_emotion ?dominant_emotion ;\r\n              ex:emotion ?emotion .\r\n\r\n  ?region ex:x ?x ;\r\n          ex:y ?y ;\r\n          ex:w ?w ;\r\n          ex:h ?h .\r\n\r\n  ?gender ex:Woman ?Woman ;\r\n          ex:Man ?Man .\r\n\r\n  ?race ex:asian ?asian ;\r\n        ex:indian ?indian ;\r\n        ex:black ?black ;\r\n        ex:white ?white ;\r\n        ex:middle_eastern ?middle_eastern ;\r\n        ex:latino_hispanic ?latino_hispanic .\r\n\r\n  ?emotion ex:angry ?angry ;\r\n           ex:disgust ?disgust ;\r\n           ex:fear ?fear ;\r\n           ex:happy ?happy ;\r\n           ex:sad ?sad ;\r\n           ex:surprise ?surprise ;\r\n           ex:neutral ?neutral .\r\n}\r\n";

            var resultSet = graph.ExecuteQuery(query) as SparqlResultSet;

            if (resultSet != null)
            {
                var results = resultSet.Select(result =>
                    result.Variables.ToDictionary(variable => variable, variable => result[variable].ToString()))
                    .ToList();

                return results;
            }
            return new List<Dictionary<string, string>>();
        }
    }
}
