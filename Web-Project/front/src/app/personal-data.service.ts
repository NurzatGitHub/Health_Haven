import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { PersonalData, Post } from './models';


@Injectable({
  providedIn: 'root'
})
export class PersonalDataService {
  private apiUrl = 'http://localhost:8000/api';

  constructor(private http: HttpClient) {}

  getUserData(): Observable<any> {
    return this.http.get<any>(`${this.apiUrl}/user_data/`);
  }
  // updateUserData(userData: PersonalData): Observable<PersonalData> {
  //   return this.http.put<PersonalData>(`${this.apiUrl}personaldataset/`, userData);
  // }

  // createPersonalData(phone_number: string): Observable<PersonalData> {
  //   return this.http.post<PersonalData>(
  //     `${this.apiUrl}personaldataset/`,
  //     {phone_number}
  //   )
  // }

  createPersonalData(formData: FormData): Observable<PersonalData> {
    const headers = new HttpHeaders();
    // Установите заголовки, если они требуются вашим сервером
    // headers.append('Content-Type', 'multipart/form-data');
    // headers.append('Accept', 'application/json');

    return this.http.post<PersonalData>(`${this.apiUrl}personaldataset/`, formData, { headers });
  }

  createCategory(name: string): Observable<any> {
    return this.http.post<any>(
      `${this.apiUrl}/personaldataset/`,
      {name}
    )
  }

  getPersonalData(): Observable<PersonalData[]> {
    return this.http.get<PersonalData[]>(
      `${this.apiUrl}personaldataset/`
    )
  }
}

// createPost(body: string): Observable<any> {
//   return this.http.post<any>(
//     `${this.apiUrl}/posts/`,
//     {body}
//   )
// }