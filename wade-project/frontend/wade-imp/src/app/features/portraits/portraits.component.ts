import { Component } from '@angular/core';
import { PortraitsService } from './portraits.service';

@Component({
  selector: 'app-portraits',
  templateUrl: './portraits.component.html',
  styleUrl: './portraits.component.scss'
})
export class PortraitsComponent {
  images: string[] = [];

  constructor(private portraitsService: PortraitsService) { }

  ngOnInit(): void {
    this.loadImages();
  }

  loadImages() {
    this.portraitsService.getImages()
      .subscribe((imageList: string[]) => {
        this.images = imageList;
      });
  }
}
