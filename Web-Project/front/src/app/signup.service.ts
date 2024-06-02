import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Data } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class SignupService {
  private apiUrl = 'http://localhost:8000';

  constructor(private http: HttpClient) { }

  // signUp(user: string, password: string): Observable<signUp> {
  //   return this.http.post<signUp>(`${this.apiUrl}/api/signup/`, {user, password});
  // }
  signUp(username: string, last_name: string, email: string, password: string): Observable<any> {
    return this.http.post<any>(`${this.apiUrl}/api/signup/`, { username, last_name, email, password });
  }
}
