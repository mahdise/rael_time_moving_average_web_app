import { TestBed } from '@angular/core/testing';

import { PullcrossoverService } from './pullcrossover.service';

describe('PullcrossoverService', () => {
  let service: PullcrossoverService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(PullcrossoverService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
