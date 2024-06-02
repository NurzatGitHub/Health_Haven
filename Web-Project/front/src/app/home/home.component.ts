
import { Component } from '@angular/core';
import { PersonalDataService } from '../personal-data.service';
import { CommonModule } from '@angular/common';
import { Post } from '../models';
import { PostService } from '../post.service';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent {
  body: string = "";
  author: string = "";
  username: string = "";
  userData: any;
  loaded = false
  personaldataset: Post[] = [];

  constructor(private personalDataService: PersonalDataService,private postService : PostService) {}

    ngOnInit(): void {
      this.personalDataService.getUserData().subscribe(data => {
        this.userData = data;
        this.author = this.userData.username
      },
      (error) => {
        console.error('Error fetching user data:', error);
      }
    );
    this.Poster();
    }

    Poster(): void {
      this.loaded = false;
      this.postService.getPosts().subscribe((personaldataset) => {
      this.personaldataset = personaldataset;
      this.loaded = true; 
    });
    }

    addCategory() {
      if (this.body !== '') {
        this.postService
          .createPost(this.body, this.author)
          .subscribe((data) => {
            this.body = "";
            this.personaldataset.push(data);
          });
      } else {
        alert("Please, enter category name.")
      }
    }
}
