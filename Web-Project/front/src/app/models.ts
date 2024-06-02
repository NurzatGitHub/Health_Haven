export interface PersonalData {
    id:                 number
    image:              string
    phone_number:       string
    date_of_birth:      string
    blood_group:        string
    diagnosis:          string
    allergies:          string
    contraindications:  string
    guardian_contact:   string
    hospital:           string
    user:               number
}

export interface Token {
    access:            string;
    refresh:           string;
  }

export interface Post {
    title: string; 
    author: string;
    body: string;
}
