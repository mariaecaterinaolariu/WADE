import { Component } from '@angular/core';
import { PortraitsService } from './portraits.service';

interface ImageDetail {
  src: string;
  width: number;
  height: number;
}

@Component({
  selector: 'app-portraits',
  templateUrl: './portraits.component.html',
  styleUrl: './portraits.component.scss'
})
export class PortraitsComponent {
  images: string[] = [];
  imageDetails: ImageDetail[] = []; // this will hold the image details including width and height
  router: any;

  constructor(private portraitsService: PortraitsService) { }

  ngOnInit(): void {
    this.loadImages();
  }

  loadImages() {
    this.portraitsService.getImages()
      .subscribe((imageList: string[]) => {
        this.images = imageList;
        console.log(this.images);
        this.loadImageDetails();
      });
  }

  loadImageDetails() {
    let maximumWidth = 0;
    let minimumWidth = 0;
    let columns = [[], [], [], [], []];
    this.images.forEach((imageSrc) => {
      let img = new Image();
      img.src = imageSrc;
      img.onload = () => {
        this.imageDetails.push({
          src: imageSrc,
          width: img.width,
          height: img.height
        });
        // get the maximum width of the images and the minimum width of the images
        if (img.width > maximumWidth) {
          maximumWidth = img.width;
        }
        // get the minimum width of the images
        if (img.width < minimumWidth) {
          minimumWidth = img.width;
        }
      };
    });
    // Now you can sort the imageDetails array based on their width
    this.imageDetails.sort((a, b) => a.width - b.width);
  }
}
