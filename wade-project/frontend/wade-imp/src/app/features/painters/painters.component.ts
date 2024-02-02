import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-painters',
  templateUrl: './painters.component.html',
  styleUrl: './painters.component.scss'
})
export class PaintersComponent implements OnInit {
  painter: any;
  image : string | null = null;
  painterImages:string[] = [];
  namePainter : string | null = null;

  constructor(
    private route: ActivatedRoute,
    private http: HttpClient,
  ) { }

  ngOnInit() {
    this.getPainter();
    this.loadImages();
  }

  getPainter(){
    let name = this.route.snapshot.paramMap.get('name');
    this.namePainter = this.route.snapshot.paramMap.get('name');
    console.log(this.namePainter);
    if (name?.includes('.jpg')) {
      console.log('The name contains .jpg');
      this.http.get(`http://127.0.0.1:5000/uploads/${name}`).subscribe((data: any) => { // Get the list of images from the server;
        this.image = data;
      });
      console.log(this.image);
    }
    name = name?.replace('.jpg', '') ?? null; // Use nullish coalescing operator
    // Replace hyphen with underscore
    name = name?.replace('-', '_') ?? null;
    name = name?.replace('-', '_') ?? null;
    // Capitalize each part
    name = name?.split('_').map(part => part.charAt(0).toUpperCase() + part.slice(1)).join('_') ?? null;
    name = name?.replace(/_\d+$/, '') ??null;

    console.log(name);
    this.http.get(`http://127.0.0.1:5000/painters/${name}`).subscribe((data: any) => {
      this.painter = data;
    });
  }

  loadImages() {
    // remake the name of the format of the files:
    this.namePainter = this.namePainter?.replace('_', '-') ?? null;
    this.http.get('http://127.0.0.1:5000/images').subscribe((data: any) => {
      this.painterImages = data.filter((image: string) => {
        //console.log(image.startsWith(this.namePainter ?? ''));
        if (image.startsWith(this.namePainter ?? '') === true)
          this.painterImages.push(image);
        return image;
      });  
    });
    console.log(this.painterImages);
    }

}
