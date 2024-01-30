import { Component } from '@angular/core';
import { UploadService } from './upload.service';

@Component({
  selector: 'app-upload',
  templateUrl: './upload.component.html',
  styleUrl: './upload.component.scss'
})
export class UploadComponent {
  selectedFile: File | null = null;

  constructor(private uploadService: UploadService) {}

  onFileSelected(event: any) {
    this.selectedFile = event.target.files[0];
  }

  uploadImage() {
    if (this.selectedFile) {
      const formData = new FormData();
      formData.append('image', this.selectedFile);
  
      this.uploadService.uploadImage(formData)
        .subscribe(
          response => {
            console.log('Image uploaded successfully:', response);
          },
          error => {
            console.error('Error uploading image:', error);
          }
        );
    } else {
      console.error('No file selected');
    }
  }
  
}
