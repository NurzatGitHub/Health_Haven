import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class PostService {

  private apiUrl = 'http://localhost:8000/api';

  constructor(private http: HttpClient) {}
  
  // createPost(body: string, author: string): Observable<any> {
  //   return this.http.post<any>(
  //     `${this.apiUrl}/posts/`,
  //     {body, author}
  //   )
  // }

  createPost(body: string, author: string): Observable<any> {
    const postData = { body, author };
    return this.http.post<any>('http://localhost:8000/api/posts/', postData);
  }
  getPosts(): Observable<any> {
    return this.http.get<any>(`${this.apiUrl}/posts/`);
  }
}
