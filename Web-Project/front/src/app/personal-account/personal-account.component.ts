import { Component, OnInit } from '@angular/core';
import { PersonalDataService } from '../personal-data.service';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { PersonalData } from '../models';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-personal-account',
  standalone: true,
  imports: [
    CommonModule,
    RouterModule,
    FormsModule,
  ],
  templateUrl: './personal-account.component.html',
  styleUrls: ['./personal-account.component.css']
  
})
export class PersonalAccountComponent implements OnInit {
  userData: any;
  personaldataset: PersonalData[] = [];
  logged: boolean = false;
  phone_number: string = "";
  image: File | null = null;

  constructor(private personalDataService: PersonalDataService) {}

    ngOnInit(): void {
      this.personalDataService.getUserData().subscribe(data => {
        this.userData = data;
      },
      (error) => {
        console.error('Error fetching user data:', error);
      }
    );

    const access = localStorage.getItem("access");
    if (access) {
      this.logged = true;
      this.getCategories();
    }
    }

    getCategories() {
      this.personalDataService
        .getPersonalData()
        .subscribe((data) => {
          this.personaldataset = data;
        });
    }
  
    // addPersonaldata() {
    //   if (this.phone_number !== '') {
    //     this.personalDataService
    //       .createPersonalData(this.phone_number)
    //       .subscribe((data) => {
    //         this.phone_number = "";
    //         this.personaldataset.push(data);
    //       });
    //   } else {
    //     alert("Please, enter phone number .")
    //   }
    // }

    addPersonaldata(): void {
      if (this.phone_number !== '' && this.image !== null) {
        const formData: FormData = new FormData();
        formData.append('phone_number', this.phone_number);
        formData.append('image', this.image);
  
        this.personalDataService.createPersonalData(formData).subscribe(
          (data: PersonalData) => {
            this.phone_number = '';
            this.image = null;
            this.personaldataset.push(data);
          },
          (error) => {
            console.error('Error adding personal data:', error);
          }
        );
      } else {
        alert('Please enter phone number and select photo.');
      }
    }

    onFileSelected(event: any): void {
      this.image = event.target.files[0] || null;
    }
    
}
