using Microsoft.OpenApi.Models;
using WebApplication1.Repositories;
using WebApplication1.Service;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
//builder.Services.AddRazorPages();

//builder.Services.AddTransient<IImageRepository, ImageRepository>();
builder.Services.AddTransient<IImageService, ImageService>();

builder.Services.AddControllers();

//builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();
var app = builder.Build();

// Configure the HTTP request pipeline.
app.UseSwagger();
app.UseSwaggerUI(options =>
{
    options.SwaggerEndpoint("/swagger/v1/swagger.json", "v1");
    options.RoutePrefix = string.Empty;
});
if (!app.Environment.IsDevelopment())
{
    app.UseDeveloperExceptionPage();

}

app.UseHttpsRedirection();
app.UseStaticFiles();

app.UseRouting();

//app.UseAuthorization();

//app.MapRazorPages();
app.MapControllers();
app.Run();
