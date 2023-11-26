namespace WebApplication1.Service
{
    public interface IImageService
    {
        IEnumerable<Dictionary<string, string>> GetImageInformation();
    }
}
