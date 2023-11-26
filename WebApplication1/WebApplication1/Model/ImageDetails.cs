namespace WebApplication1.Model
{
    class ImageDetails
    {
        public int age { get; set; }
        public Region region { get; set; }
        public Gender gender { get; set; }
        public string dominant_gender { get; set; }
        public Race race { get; set; }
        public string dominant_race { get; set; }
        public Emotion emotion { get; set; }
        public string dominant_emotion { get; set; }
    }

    class Region
    {
        public int x { get; set; }
        public int y { get; set; }
        public int w { get; set; }
        public int h { get; set; }
    }

    class Gender
    {
        public double Woman { get; set; }
        public double Man { get; set; }
    }

    class Race
    {
        public double asian { get; set; }
        public double indian { get; set; }
        public double black { get; set; }
        public double white { get; set; }
        public double middle_eastern { get; set; }
        public double latino_hispanic { get; set; }
    }

    class Emotion
    {
        public double angry { get; set; }
        public double disgust { get; set; }
        public double fear { get; set; }
        public double happy { get; set; }
        public double sad { get; set; }
        public double surprise { get; set; }
        public double neutral { get; set; }
    }
}
