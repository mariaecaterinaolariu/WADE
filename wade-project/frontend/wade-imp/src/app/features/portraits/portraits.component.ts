import { Component } from '@angular/core';
import { PortraitsService } from './portraits.service';

interface ImageDetail {
  src: string;
  width: number;
  height: number;
}

interface Filter {
  label: string;
  value: string;
  checked: boolean;
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

  emotions: Filter[] = [
    { label: 'Angry', value: 'Angry', checked: false },
    { label: 'Disgust', value: 'Disgust', checked: false },
    { label: 'Fear', value: 'Fear', checked: false },
    { label: 'Happy', value: 'Happy', checked: false },
    { label: 'Sad', value: 'Sad', checked: false },
    { label: 'Surprise', value: 'Surprise', checked: false },
    { label: 'Neutral', value: 'Neutral', checked: false },
  ];

  genders: Filter[] = [
    { label: 'Male', value: 'Male', checked: false },
    { label: 'Female', value: 'Female', checked: false }
  ];

  races: Filter[] = [
    { label: 'White', value: 'White', checked: false },
    { label: 'Latino hispanic', value: 'LatinoHispanic', checked: false },
    { label: 'Asian', value: 'asian', checked: false },
    { label: 'Black', value: 'black', checked: false },
    { label: 'Indian', value: 'indian', checked: false },
    { label: 'Middle eastern', value: 'middle eastern', checked: false },
  ];

  ngOnInit(): void {
    this.loadImages();
  }

  toggleFilter(filter: Filter) {
    filter.checked = !filter.checked;
    this.updateFilteredImages();
  }

  private updateFilteredImages() {
    const checkedFilters = this.getCheckedFilters();
    if (checkedFilters) {
      this.portraitsService.getFilteredImages(checkedFilters).subscribe(
        (response) => {
          console.log(response)
          this.images = response.images;
        },
        (error) => {
          console.error('Error fetching images:', error);
        }
      );
    }
    else{
      this.loadImages();
    }
  }

  private getCheckedFilters(): {emotion: string[], gender: string[], race: string[]} | null {
    const checkedEmotions = this.emotions.filter(f => f.checked).map(f => f.value);
    const checkedGenders = this.genders.filter(f => f.checked).map(f => f.value);
    const checkedRaces = this.races.filter(f => f.checked).map(f => f.value);

    if (checkedEmotions.length === 0 && checkedGenders.length === 0 && checkedRaces.length === 0) {
      return null;
    }

    return { emotion: checkedEmotions, gender: checkedGenders, race: checkedRaces };
  }
  
  loadImages() {
    this.portraitsService.getImages()
      .subscribe((imageList: string[]) => {
        this.images = imageList;
        //console.log(this.images);
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
        if (img.width > maximumWidth) {
          maximumWidth = img.width;
        }
        if (img.width < minimumWidth) {
          minimumWidth = img.width;
        }
      };
    });
    this.imageDetails.sort((a, b) => a.width - b.width);
  }
}
