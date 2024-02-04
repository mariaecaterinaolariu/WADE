import { Component, ElementRef, ViewChild, inject } from '@angular/core';
import { PortraitsService } from './portraits.service';
import { MatAutocompleteSelectedEvent } from '@angular/material/autocomplete';
import { MatChipInputEvent } from '@angular/material/chips';
import { Observable, map, startWith } from 'rxjs';
import { FormControl } from '@angular/forms';

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
  imageDetails: ImageDetail[] = []; 
  router: any;
  separatorKeysCodes: number[] = [13,188];
  painters: string[] = [];
  allPainters: string[] = [];

  visible = true;
  removable = true;
  addOnBlur = false;

  formCtrl = new FormControl('');
  filteredPainters: Observable<string[]>;
  noImagesMessage = '';

  @ViewChild('painterInput') painterInput!: ElementRef<HTMLInputElement>;

  constructor(private portraitsService: PortraitsService) {
    this.filteredPainters = this.formCtrl.valueChanges.pipe(
      startWith(null),
      map((painter: string | null) => (painter ? this._filter(painter) : this.allPainters.slice()))
    );
  }


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
    this.getPainters();
  }

  getPainters(){
    this.portraitsService.getPainterName().subscribe(response=>{
      this.allPainters = response;
    });
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

  private getCheckedFilters(): {emotion: string[], gender: string[], race: string[], painter: string[]} | null {
    const checkedEmotions = this.emotions.filter(f => f.checked).map(f => f.value);
    const checkedGenders = this.genders.filter(f => f.checked).map(f => f.value);
    const checkedRaces = this.races.filter(f => f.checked).map(f => f.value);

    if (checkedEmotions.length === 0 && checkedGenders.length === 0 && checkedRaces.length === 0 && this.painters.length === 0) {
      return null;
    }

    return { emotion: checkedEmotions, gender: checkedGenders, race: checkedRaces, painter: this.painters };
  }
  
  loadImages() {
    this.portraitsService.getImages()
      .subscribe((imageList: string[]) => {
        this.images = imageList;
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

  add(event: MatChipInputEvent): void {
    const value = (event.value || '').trim();

    if (value) {
      this.painters.push(value);
    }

    event.chipInput!.clear();
    this.formCtrl.setValue(null);
    console.log(this.painters);
    this.updateFilteredImages();
  }

  remove(painter: string): void {
    const index = this.painters.indexOf(painter);

    if (index >= 0) {
      this.painters.splice(index, 1);
    }
    this.updateFilteredImages();
  }

  selected(event: MatAutocompleteSelectedEvent): void {
    this.painters.push(event.option.viewValue);
    console.log(this.painters);
    this.updateFilteredImages();
    this.painterInput.nativeElement.value = '';
    this.formCtrl.setValue(null);
  }

  private _filter(value: string): string[] {
    const filterValue = value.toLowerCase();
    return this.allPainters.filter(painter => painter.toLowerCase().includes(filterValue));
  }
}
