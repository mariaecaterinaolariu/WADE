import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class PortraitsService {

  constructor(private http: HttpClient) { }

  getImages(): Observable<any> {
    return this.http.get('http://127.0.0.1:5000/images');
  }


  getFilteredImages(filters: {emotion: string[], gender: string[], race: string[]}): Observable<any> {
    let params = new HttpParams();

    if (filters.emotion.length > 0) {
      params = params.set('emotion', filters.emotion.join(','));
    }

    if (filters.gender.length > 0) {
      params = params.set('gender', filters.gender.join(','));
    }

    if (filters.race.length > 0) {
      params = params.set('race', filters.race.join(','));
    }
    console.log(params)
    return this.http.get('http://127.0.0.1:5000/filter', { params });
  }
}