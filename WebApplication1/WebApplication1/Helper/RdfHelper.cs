using System;
using System.Collections.Generic;
using Newtonsoft.Json;
using JsonLD.Core;
using Newtonsoft.Json.Linq;
using WebApplication1.Model;
using VDS.RDF;
using RDFSharp.Model;

public static class RdfHelper
{
    public static void SaveAsRDF()
    {
        string jsonContent = System.IO.File.ReadAllText("Files\\facedetect.json");
        var data = JsonConvert.DeserializeObject<List<ImageDetails>>(jsonContent);

        var context = new
        {
            age = "http://example.org/age",
            region = new { x = "http://example.org/x", y = "http://example.org/y", w = "http://example.org/w", h = "http://example.org/h" },
            gender = new { Woman = "http://example.org/Woman", Man = "http://example.org/Man" },
            dominant_gender = "http://example.org/dominant_gender",
            race = new { asian = "http://example.org/asian", indian = "http://example.org/indian", black = "http://example.org/black", white = "http://example.org/white", middle_eastern = "http://example.org/middle_eastern", latino_hispanic = "http://example.org/latino_hispanic" },
            dominant_race = "http://example.org/dominant_race",
            emotion = new { angry = "http://example.org/angry", disgust = "http://example.org/disgust", fear = "http://example.org/fear", happy = "http://example.org/happy", sad = "http://example.org/sad", surprise = "http://example.org/surprise", neutral = "http://example.org/neutral" },
            dominant_emotion = "http://example.org/dominant_emotion"
        };

        var rdfGraph = new RDFGraph();
                // Define RDF vocabulary
var rdfVocabulary = new RDFNamespace("ex", "http://example.org/");

foreach (var item in data)
{
    var subjectNode = new RDFResource($"{rdfVocabulary}{item.age}");

    // Add triples for age, region, gender, race, emotion, etc.
    rdfGraph.AddTriple(new RDFTriple(subjectNode, new RDFResource(rdfVocabulary + "age"), new RDFPlainLiteral(item.age.ToString())));

    // Convert region object to RDF triples
    var regionNode = new RDFResource($"{rdfVocabulary}region");
    rdfGraph.AddTriple(new RDFTriple(subjectNode, new RDFResource(rdfVocabulary + "region"), regionNode));
    rdfGraph.AddTriple(new RDFTriple(regionNode, new RDFResource(rdfVocabulary + "x"), new RDFPlainLiteral(item.region.x.ToString())));
    rdfGraph.AddTriple(new RDFTriple(regionNode, new RDFResource(rdfVocabulary + "y"), new RDFPlainLiteral(item.region.y.ToString())));
    rdfGraph.AddTriple(new RDFTriple(regionNode, new RDFResource(rdfVocabulary + "w"), new RDFPlainLiteral(item.region.w.ToString())));
    rdfGraph.AddTriple(new RDFTriple(regionNode, new RDFResource(rdfVocabulary + "h"), new RDFPlainLiteral(item.region.h.ToString())));

    rdfGraph.AddTriple(new RDFTriple(subjectNode, new RDFResource(rdfVocabulary + "dominant_gender"), new RDFPlainLiteral(item.dominant_gender)));

    // Convert gender object to RDF triples
    var genderNode = new RDFResource($"{rdfVocabulary}gender");
    rdfGraph.AddTriple(new RDFTriple(subjectNode, new RDFResource(rdfVocabulary + "gender"), genderNode));
    rdfGraph.AddTriple(new RDFTriple(genderNode, new RDFResource(rdfVocabulary + "Woman"), new RDFPlainLiteral(item.gender.Woman.ToString())));
    rdfGraph.AddTriple(new RDFTriple(genderNode, new RDFResource(rdfVocabulary + "Man"), new RDFPlainLiteral(item.gender.Man.ToString())));

    rdfGraph.AddTriple(new RDFTriple(subjectNode, new RDFResource(rdfVocabulary + "dominant_race"), new RDFPlainLiteral(item.dominant_race)));

    // Convert race object to RDF triples
    var raceNode = new RDFResource($"{rdfVocabulary}race");
    rdfGraph.AddTriple(new RDFTriple(subjectNode, new RDFResource(rdfVocabulary + "race"), raceNode));
    rdfGraph.AddTriple(new RDFTriple(raceNode, new RDFResource(rdfVocabulary + "asian"), new RDFPlainLiteral(item.race.asian.ToString())));
    rdfGraph.AddTriple(new RDFTriple(raceNode, new RDFResource(rdfVocabulary + "indian"), new RDFPlainLiteral(item.race.indian.ToString())));
    rdfGraph.AddTriple(new RDFTriple(raceNode, new RDFResource(rdfVocabulary + "black"), new RDFPlainLiteral(item.race.black.ToString())));
    rdfGraph.AddTriple(new RDFTriple(raceNode, new RDFResource(rdfVocabulary + "white"), new RDFPlainLiteral(item.race.white.ToString())));
    rdfGraph.AddTriple(new RDFTriple(raceNode, new RDFResource(rdfVocabulary + "middle_eastern"), new RDFPlainLiteral(item.race.middle_eastern.ToString())));
    rdfGraph.AddTriple(new RDFTriple(raceNode, new RDFResource(rdfVocabulary + "latino_hispanic"), new RDFPlainLiteral(item.race.latino_hispanic.ToString())));

    rdfGraph.AddTriple(new RDFTriple(subjectNode, new RDFResource(rdfVocabulary + "dominant_emotion"), new RDFPlainLiteral(item.dominant_emotion)));

    // Convert emotion object to RDF triples
    var emotionNode = new RDFResource($"{rdfVocabulary}emotion");
    rdfGraph.AddTriple(new RDFTriple(subjectNode, new RDFResource(rdfVocabulary + "emotion"), emotionNode));
    rdfGraph.AddTriple(new RDFTriple(emotionNode, new RDFResource(rdfVocabulary + "angry"), new RDFPlainLiteral(item.emotion.angry.ToString())));
    rdfGraph.AddTriple(new RDFTriple(emotionNode, new RDFResource(rdfVocabulary + "disgust"), new RDFPlainLiteral(item.emotion.disgust.ToString())));
    rdfGraph.AddTriple(new RDFTriple(emotionNode, new RDFResource(rdfVocabulary + "fear"), new RDFPlainLiteral(item.emotion.fear.ToString())));
    rdfGraph.AddTriple(new RDFTriple(emotionNode, new RDFResource(rdfVocabulary + "happy"), new RDFPlainLiteral(item.emotion.happy.ToString())));
    rdfGraph.AddTriple(new RDFTriple(emotionNode, new RDFResource(rdfVocabulary + "sad"), new RDFPlainLiteral(item.emotion.sad.ToString())));
    rdfGraph.AddTriple(new RDFTriple(emotionNode, new RDFResource(rdfVocabulary + "surprise"), new RDFPlainLiteral(item.emotion.surprise.ToString())));
    rdfGraph.AddTriple(new RDFTriple(emotionNode, new RDFResource(rdfVocabulary + "neutral"), new RDFPlainLiteral(item.emotion.neutral.ToString())));
}

        SaveRdfGraph(rdfGraph, "Files\\output.rdf", RDFModelEnums.RDFFormats.RdfXml);
    }

    static void SaveRdfGraph(RDFGraph rdfGraph, string fileName, RDFModelEnums.RDFFormats format)
    {
        rdfGraph.ToFile(format,fileName);
        Console.WriteLine($"RDF graph saved to {fileName}");
    }
}
