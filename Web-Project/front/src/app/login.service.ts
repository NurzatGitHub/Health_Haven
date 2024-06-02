import {Injectable,Inject} from '@angular/core';
import {Observable} from "rxjs";
import {PersonalData, Token} from "./models";
import {HttpClient} from "@angular/common/http";
import { AsyncLocalStorage } from 'async_hooks';

@Injectable({
  providedIn: 'root'
})
export class LoginService {
  BASE_URL = 'http://localhost:8000';

  constructor(private http: HttpClient, ) {
  }

  login(username: string, password: string): Observable<any> {
    return this.http.post<any>(
      `${this.BASE_URL}/api/login/`,
      {username, password}
    )
  }

  getPersonalDataset(): Observable<PersonalData[]> {
    return this.http.get<PersonalData[]>(
      `${this.BASE_URL}/api/personaldataset/`
    )
  }

  createPersonalData(name: string): Observable<PersonalData> {
    return this.http.post<PersonalData>(
      `${this.BASE_URL}/api/personaldataset/`,
      {name}
    )
  }
}