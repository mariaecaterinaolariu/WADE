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
  image : any;

  constructor(
    private route: ActivatedRoute,
    private http: HttpClient
  ) { }

  ngOnInit() {
    let name = this.route.snapshot.paramMap.get('name');
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
    // this.http.get('http://127.0.0.1:5000/uploads').subscribe((data: any) => {
    //   this.images = data.filter((image: any) => image.includes(name ?? ''));
    // });
  }

}
