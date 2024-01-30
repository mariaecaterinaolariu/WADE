import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class PortraitsService {

  constructor(private http: HttpClient) { }

  getImages(): Observable<any> {
    return this.http.get('http://127.0.0.1:5000/images');
  }

}