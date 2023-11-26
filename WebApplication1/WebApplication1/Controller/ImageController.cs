using Microsoft.AspNetCore.Mvc;
using VDS.RDF.Query.Algebra;
using WebApplication1.Service;

namespace WebApplication1.Controller;

[ApiController]
[Route("api/[controller]")]
public class ImageController : ControllerBase
{
    private readonly IImageService service;

    public ImageController(IImageService service)
    {
        this.service = service;
    }

    [HttpGet("image-details")]
    public IActionResult Get()
    {
        var jsonLd = this.service.GetImageInformation();

        return this.Ok(jsonLd);
    }
}
