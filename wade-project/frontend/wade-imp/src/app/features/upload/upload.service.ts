import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UploadService {

  constructor(private http: HttpClient) { }

  uploadImage(imageFile: FormData): Observable<any> {
    return this.http.post<any>('http://127.0.0.1:5000/upload-image', imageFile);
  }
}
