import { ChangeDetectorRef, Component } from '@angular/core';
import { UploadService } from './upload.service';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-upload',
  templateUrl: './upload.component.html',
  styleUrl: './upload.component.scss'
})
export class UploadComponent {
  selectedFile: File | null = null;
  formData : FormData = new FormData();
  image: any;
  fileName : string = "";
  responseUpload: string = "";
  emotions: any;

  constructor(private uploadService: UploadService, 
    private cdr: ChangeDetectorRef,
    private http: HttpClient) {}

  onFileSelected(event: any) {
    this.selectedFile = event.target.files[0];
  }

  uploadImage() {
    if (this.selectedFile) {
      //const formData = new FormData();
      this.formData.append('image', this.selectedFile);
      this.fileName = this.selectedFile.name;
  
      this.uploadService.uploadImage(this.formData)
        .subscribe(
          response => {
            this.responseUpload = 'Image uploaded successfully';
            console.log('Image uploaded successfully:', response);
          },
          error => {
            console.error('Error uploading image:', error);
          }
        );
    } else {
      console.error('No file selected');
    }
    if(this.responseUpload == 'Image uploaded successfully'){
      var x = document.getElementById("information");
      if (x){
        if (x.style.display === "none") {
          x.style.display = "block";
        } else {
          x.style.display = "none";
        }
      }
    }
    
  }
  getImageInfo(){
    console.log("INSIDE GET INFO")
    console.log(this.formData.get('image'));
    let name = this.fileName;
    console.log(name);
    console.log(this.emotions);
      if(this.fileName){
        console.log("not null image")
        var x = document.getElementById("imageDiv");
        if (x){
          if (x.style.display === "none") {
            x.style.display = "block";
          } else {
            x.style.display = "none";
          }
        }
      }
      // Trigger change detection manually
      // this.cdr.detectChanges();
  }

  getEmotions(){
    let name = this.fileName
    this.http.get(`http://127.0.0.1:5000/analyze/emotions/${name}`).subscribe((data: any) => {
      this.emotions = data[0];
    });
    console.log(this.emotions);
  }

}
